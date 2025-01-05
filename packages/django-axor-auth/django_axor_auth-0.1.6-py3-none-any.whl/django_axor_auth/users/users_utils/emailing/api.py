from django_axor_auth.configurator import config
from django_axor_auth.users.users_utils.emailing.templates.email_changed import email_changed_template
from django_axor_auth.users.users_utils.emailing.templates.resend_verification_email import email_verification_template
from django_axor_auth.utils.emailing.helper import email_send_helper
from .templates.forgot_password import forgot_password_template
from .templates.magic_link import magic_link_template
from .templates.new_user_account import new_user_account_template
from .templates.reset_password_success import reset_password_success_template


def send_welcome_email(first_name: str, verification_url: str, email: str) -> int:
	"""
	Send a welcome email to a new user

	:param first_name: User's first name
	:param verification_url: URL for verifying user email
	:param email: E-mail address to send the email to

	:return: 0 if fails
	:rtype: int
	"""
	template = new_user_account_template(first_name, verification_url)
	return email_send_helper(
		email_to=email,
		subject='Welcome to ' + config.APP_NAME,
		plain_message=f"Hello {first_name},\n\nPlease verify your email by clicking the link below.\n\n{verification_url}",
		html_message=template
	)


def send_forgot_password_email(first_name: str, reset_url: str, email: str, ip: str,
							   subject='Reset your password') -> int:
	"""
	Send a welcome email to a new user

	:param first_name: User's first name
	:param reset_url: URL for resetting password
	:param email: User's email address
	:param ip: IP address that made this request
	:param subject: Optional

	:return: 0 if fails
	:rtype: int
	"""
	template = forgot_password_template(first_name, reset_url, ip, subject)
	return email_send_helper(
		email_to=email,
		subject=subject,
		plain_message=f"Hello {first_name},\n\nPlease reset your password by clicking the link below.\n\n{reset_url}",
		html_message=template
	)


def send_password_changed_email(first_name: str, email: str, subject='Password was changed'):
	"""
	Send a welcome email to a new user

	:param first_name: User's first name
	:param email: User's email address
	:param subject: Optional

	:return: 0 if fails
	:rtype: int
	"""
	template = reset_password_success_template(first_name, subject)
	message = f"Hello {first_name},\n\nYour password was successfully changed. If you did not make this change, please contact our support immediately."
	return email_send_helper(
		email_to=email,
		subject=subject,
		plain_message=message,
		html_message=template
	)


def send_email_changed_email(first_name: str, verification_url: str, email: str, subject='Email Changed Successfully!'):
	"""
	Send a welcome email to a new user

	:param first_name: User's first name
	:param verification_url: URL for e-mail verification
	:param email: User's email address
	:param subject: Optional

	:return: 0 if fails
	:rtype: int
	"""
	template = email_changed_template(first_name, verification_url, subject)
	return email_send_helper(
		email_to=email,
		subject=subject,
		plain_message=f"Hello {first_name},\n\nPlease verify your new email by clicking the link below.\n\n{verification_url}",
		html_message=template
	)


def send_magic_link_email(first_name: str, url: str, email: str, subject='Sign in with Magic Link'):
	"""
	Send a welcome email to a new user

	:param first_name: User's first name
	:param url: URL for signing in
	:param email: User's email address
	:param subject: Optional

	:return: 0 if fails
	:rtype: int
	"""
	template = magic_link_template(first_name, url, subject)
	return email_send_helper(
		email_to=email,
		subject=subject,
		plain_message=f"Hello {first_name},\n\nYour magic link is ready!\n\n{url}",
		html_message=template
	)


def send_verification_email(first_name: str, verification_url: str, email: str, subject='Verify your email'):
	"""
	Send a welcome email to a new user

	:param first_name: User's first name
	:param verification_url: URL for verifying e-mail
	:param email: User's email address
	:param subject: Optional

	:return: 0 if fails
	:rtype: int
	"""
	template = email_verification_template(first_name, verification_url)
	return email_send_helper(
		email_to=email,
		subject=subject,
		plain_message=f"Hello {first_name},\n\nPlease verify your email by clicking the link below.\n\n{verification_url}",
		html_message=template
	)
