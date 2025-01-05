import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_str

from django_axor_auth.configurator import config
from django_axor_auth.users.api import get_request_user
from django_axor_auth.users.users_forgot_password.views import forgot_password, reset_password, _check_health
from django_axor_auth.users.users_magic_link.views import consume_magic_link, request_magic_link
from django_axor_auth.users.users_totp.api import has_totp
from django_axor_auth.users.users_totp.views import totp_init, totp_enable
from django_axor_auth.users.views import login, me, logout, verify_email, register
from .forms import SignInForm, ProcessMagicLinkForm, ForgotPasswordForm, ProcessForgotPasswordForm, TotpForm, \
	RegisterForm

app_info = dict(
	app_name=config.APP_NAME,
	app_logo=config.APP_LOGO
)


# Register Page
# -----------------------------------------------------------------------------
def register_page(request):
	template = 'register.html'
	redirect_url = request.GET.get('redirect')
	form = RegisterForm()
	# Set the request source
	request.requested_by = 'web'
	# Check if user is already signed in
	user = get_request_user(request)
	if user is not None:
		return redirect(redirect_url or 'login')
	# Check if registration is enabled
	if not config.IS_REGISTRATION_ENABLED:
		return redirect(redirect_url or 'login')
	# Check if there is a sign in request
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			api_res = register(request)
			if api_res.status_code >= 400:
				error = json.loads(api_res.content).get('detail').get('non_field_errors')[0]
				return render(request, template,
							  {'app': app_info, 'form': form, 'error': error, 'redirect': redirect_url})
			# Registration successful
			response = render(request, template, {'app': app_info, 'success': True, 'redirect': redirect_url})
			response.cookies = api_res.cookies
			return response
		pass
	return render(request, template, {'app': app_info, 'form': form, 'redirect': redirect_url})


# Sign In Page
# -----------------------------------------------------------------------------
def sign_in_page(request):
	template = 'sign_in.html'
	redirect_url = request.GET.get('redirect')
	if redirect_url is None:
		redirect_url = ''
	# Set the request source
	request.requested_by = 'web'
	# Check if there is a sign in request
	if request.method == "POST":
		form = SignInForm(request.POST)
		# Check if it was passwordless sign in
		is_passwordless = request.GET.get('method') == 'passwordless'
		if not is_passwordless and form.is_valid():
			request.data = form.cleaned_data
			api_res = login(request)
			if api_res.status_code >= 400:
				error = json.loads(api_res.content).get('title')
				error_code = json.loads(api_res.content).get('code')
				# Check if the error is due to TOTP requirement
				print(error_code)
				if api_res.status_code == 401 and 'TOTPRequired' in error_code:
					return render(request, template, {'app': app_info, 'totp': True, 'form': form,
													  'registration_enabled': config.IS_REGISTRATION_ENABLED,
													  'redirect': redirect_url})
				elif api_res.status_code == 401 and 'TOTPIncorrect' in error_code:
					return render(request, template, {'app': app_info, 'totp': True, 'form': form,
													  'registration_enabled': config.IS_REGISTRATION_ENABLED,
													  'redirect': redirect_url, 'error': error})
				# Give user the error message
				return render(request, template, {'app': app_info, 'error': error, 'form': form,
												  'registration_enabled': config.IS_REGISTRATION_ENABLED,
												  'redirect': redirect_url})
			else:
				# User is signed in
				response = render(request, template,
								  {'app': app_info, 'success': True, 'redirect': redirect_url,
								   'registration_enabled': config.IS_REGISTRATION_ENABLED})
				response.cookies = api_res.cookies
				return response
		elif is_passwordless:
			# Passwordless sign in
			email = force_str(form.data.get('email'))
			request.data = {'email': email}
			request_magic_link(request)
			return render(request, template,
						  {'app': app_info, 'success': True, 'passwordless': True, 'redirect': redirect_url})
		return render(request, template, {'app': app_info, 'error': 'Please enter email and password.', 'form': form,
										  'passwordless': is_passwordless,
										  'registration_enabled': config.IS_REGISTRATION_ENABLED,
										  'redirect': redirect_url})
	else:
		# Check if user is already signed in
		user = me(request)
		if user.status_code < 400:
			return render(request, template,
						  {'app': app_info, 'success': True, 'redirect': redirect_url,
						   'registration_enabled': config.IS_REGISTRATION_ENABLED})
		else:
			# User is not signed in
			form = SignInForm()
			# Check if ?method=passwordless is in the URL
			if request.GET.get('method') == 'passwordless':
				return render(request, template, {'app': app_info, 'passwordless': True, 'form': form,
												  'registration_enabled': config.IS_REGISTRATION_ENABLED,
												  'redirect': redirect_url})
			# default
			return render(request, template,
						  {'app': app_info, 'form': form, 'registration_enabled': config.IS_REGISTRATION_ENABLED,
						   'redirect': redirect_url})


# Logout
# -----------------------------------------------------------------------------
def sign_out_page(request):
	template = 'sign_out.html'
	redirect_url = request.GET.get('redirect')
	referrer = request.GET.get('referrer')
	if redirect_url is None:
		redirect_url = reverse('login')
	if referrer is None or len(referrer) < 1:
		referrer = request.META.get('HTTP_REFERER')
	if request.method == "POST":
		request.requested_by = 'web'
		logout(request)
		return render(request, template, {'app': app_info, 'success': True, 'redirect': redirect_url})
	return render(request, template, {'app': app_info, 'referrer': referrer})


def forgot_password_page(request):
	template = 'forgot_password.html'
	redirect_url = request.GET.get('redirect')
	if redirect_url is None:
		redirect_url = ''
	if request.method == "POST":
		form = ForgotPasswordForm(request.POST)
		if form.is_valid():
			request.requested_by = 'web'
			# Send email to user
			forgot_password(request)
			return render(request, template, {'app': app_info, 'success': True, 'redirect': redirect_url})
	return render(request, template, {'app': app_info, 'form': ForgotPasswordForm(), 'redirect': redirect_url})


def process_forgot_password(request):
	template = 'process_forgot_password.html'
	token = request.GET.get('token')
	# Process the password reset
	if request.method == "POST":
		form = ProcessForgotPasswordForm(request.POST)
		if form.is_valid():
			request.requested_by = 'web'
			request.data = form.cleaned_data
			api_res = reset_password(request)
			if api_res.status_code >= 400:
				try:
					error = json.loads(api_res.content).get('detail').get('non_field_errors')[0]
				except:
					error = json.loads(api_res.content).get('title')
				error_code = json.loads(api_res.content).get('code')
				if error_code == "HealthCheckFailed":
					return render(request, template, {'app': app_info, 'fatal_error': error})
				return render(request, template, {'app': app_info, 'error': error, 'parse': True, 'form': form})
			else:
				return render(request, template, {'app': app_info, 'success': True})
		return render(request, template,
					  {'app': app_info, 'error': 'Please enter passwords correctly.', 'parse': True, 'form': form})
	# Check if the token is valid
	if not token or not _check_health(token):
		return render(request, template, {'app': app_info,
										  'fatal_error': 'Token is not present or invalid. Please try requesting a new link.'})
	# Return the form
	form = ProcessForgotPasswordForm(initial={'token': token})
	return render(request, template, {'app': app_info, 'form': form, 'parse': True})


# Magic Link or Passwordless Login
# This is the URL that is sent to the user's email
# -----------------------------------------------------------------------------
def process_magic_link(request):
	template = 'process_magic_link.html'
	# Set the request source
	request.requested_by = 'web'
	# Sanitize the token
	token = request.GET.get('token')
	# Check if user is already signed in
	if request.method == "GET":
		user = me(request)
		if user.status_code < 400:
			return render(request, template, {'app': app_info, 'success': True})
	if token:
		form = ProcessMagicLinkForm(initial={'token': token})
		if request.method == "POST":
			api_res = consume_magic_link(request)
			if api_res.status_code >= 400:
				error = json.loads(api_res.content).get('title')
				error_code = json.loads(api_res.content).get('code')
				# Check if the error is due to TOTP requirement
				if api_res.status_code == 401 and 'TOTP' in error_code:
					return render(request, template, {'app': app_info, 'totp': True, 'form': form})
				# Give user the error message
				return render(request, template, {'app': app_info, 'error': error, 'form': None})
			else:
				# User is signed in
				response = render(request, template, {'app': app_info, 'success': True})
				response.cookies = api_res.cookies
				return response
		return render(request, template, {'app': app_info, 'form': form, 'load': True})
	else:
		return render(request, template, {'app': app_info, 'error': 'Token is required.'})


def process_verify_email(request):
	template = 'process_verify_email.html'
	# Set the request source
	request.requested_by = 'web'
	token = request.GET.get('token')
	# Check if user is already signed in
	if token:
		if request.method == "POST":
			api_res = verify_email(request)
			if api_res.status_code >= 400:
				error = json.loads(api_res.content).get('title')
				# Give user the error message
				return render(request, template, {'app': app_info, 'error': error})
			else:
				# Verified
				return render(request, template, {'app': app_info, 'success': True})
		return render(request, template, {'app': app_info, 'token': token})
	else:
		return render(request, template, {'app': app_info, 'error': 'Token is required.'})


# TOTP Enroll Page
# -----------------------------------------------------------------------------
def totp_enroll_page(request):
	template = 'enroll_totp.html'
	redirect_url = request.GET.get('redirect')
	# Set the request source
	request.requested_by = 'web'
	# Check if user is signed in
	user = get_request_user(request)
	# Check if user is signed in
	if user is None:
		# Redirect to sign in page
		return redirect('login')
	# Check if user has TOTP enabled
	if has_totp(user):
		return render(request, template,
					  {'app': app_info, 'success': True, 'redirect': redirect_url, 'state': 'ENABLED'})
	# Initialize TOTP
	if request.method == "POST":
		code = request.POST.get('code')
		if not code:
			api_res = totp_init(request)
			if api_res.status_code >= 400:
				error = json.loads(api_res.content).get('title')
				return render(request, template, {'app': app_info, 'fatal_error': error, 'state': 'FAILED'})
			else:
				content = api_res.data
				return render(request, template, {
					'app': app_info,
					'success': False,
					'redirect': redirect_url,
					'key': content.get('key'),
					'provision_key': content.get('provision'),
					'backup_codes': content.get('backup_codes'),
					'form': TotpForm(),
					'state': 'INITIALIZED'
				})
		else:
			api_res = totp_enable(request)
			if api_res.status_code >= 400:
				error = json.loads(api_res.content).get('title')
				return render(request, template, {'app': app_info, 'error': error, 'form': TotpForm()})
			else:
				return render(request, template,
							  {'app': app_info, 'success': True, 'redirect': redirect_url, 'state': 'ENABLED'})
	return render(request, template, {'app': app_info})
