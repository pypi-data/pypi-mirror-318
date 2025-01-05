import logging

from django.core.mail import send_mail, get_connection

from django_axor_auth.configurator import config


def email_send_helper(email_to: str, subject: str, plain_message: str, html_message: str) -> int:
	"""
	Sends email to the given email address with the given subject and template

    :param str plain_message: Plain text message to send
    :param str email_to: Address to send the email to
    :param str subject: Subject of the email
    :param str html_message: HTML template to send (See utils/emailing/base_template.py)

	:return: 1 = Success, 0 = Failure
	:rtype: int
	"""
	# Send this token
	try:
		with _get_email_connection() as connection:
			from_email = config.SMTP_DEFAULT_SEND_FROM
			return send_mail(subject=subject,
							 message=plain_message,
							 html_message=html_message,
							 from_email=from_email,
							 recipient_list=[email_to, ],
							 connection=connection)
	except Exception as e:
		logging.exception("Failed to send email to user.")
		return 0


def _get_email_connection():
	if config.SMTP_USE_TLS:
		return get_connection(
			host=config.SMTP_HOST,
			port=config.SMTP_PORT,
			username=config.SMTP_USER,
			password=config.SMTP_PASSWORD,
			use_tls=True,
		)
	else:
		return get_connection(
			host=config.SMTP_HOST,
			port=config.SMTP_PORT,
			username=config.SMTP_USER,
			password=config.SMTP_PASSWORD,
			use_ssl=True,
		)
