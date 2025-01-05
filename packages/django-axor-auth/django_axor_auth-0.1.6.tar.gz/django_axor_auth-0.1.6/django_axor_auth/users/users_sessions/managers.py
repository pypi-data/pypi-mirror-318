from datetime import timedelta

from django.db import models
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.timezone import now

from django_axor_auth.configurator import config
from .utils import generate_session_key, hash_this, getClientIP, getUserAgent


class SessionManager(models.Manager):
	"""Manages the sessions for the users
	- Create a session: Key generation and expiry
	- Delete a session: Invalidating sessions
	- Get a session: Retrieve a session by key, user, or id
	"""

	def __init__(self):
		super().__init__()
		# Session expiry in days
		self.KEY_EXPIRE_IN_SECONDS = config.AUTH_COOKIE_AGE

	def create_session(self, user, request):
		"""Primary use case: Create a session on signup/login

		Args:
			user (User): User to create session for
			request (HttpRequest): For IP and User-Agent

		Returns:
			tuple(key: str, session: Session)
		"""
		# Disable previous sessions if required
		if config.ALWAYS_DISABLE_PREVIOUS_SESSIONS:
			self.filter(user=user, is_valid=True).update(is_valid=False)
		# Create a new session
		key = generate_session_key()
		session = self.create(
			user=user,
			key=hash_this(key),
			ip=getClientIP(request),
			ua=getUserAgent(request),
			expire_at=now() + timedelta(seconds=self.KEY_EXPIRE_IN_SECONDS)
		)
		return urlsafe_base64_encode(key.encode("ascii")), session

	def delete_session(self, user, session_id):
		"""Primary use case: Logout a user

		Args:
			user (User): Model object
			session_id (uuid): The row id of the session
		"""
		try:
			session = self.get(user=user, id=session_id, is_valid=True)
			if session.is_valid:
				session.is_valid = False
				session.updated_at = now()
				session.save()
				return True
		except Exception as e:
			return False
		return False

	def authenticate_session(self, key, ip, ua):
		"""This function authenticates a user request

		Args:
			key (str): Session key

		Returns:
			Session or None
		"""
		try:
			key = urlsafe_base64_decode(key).decode("ascii")
			session = self.select_related('user').get(
				key=hash_this(key),
				is_valid=True
			)
			if session.expire_at < now():
				session.is_valid = False
				session.updated_at = now()
				session.save()
				return None
			if session.ip != ip or session.ua != ua:
				session.ip = ip
				session.ua = ua
				session.updated_at = now()
				session.save()
			return session
		except Exception as e:
			return None

	def get_session_if_valid(self, user, session_id):
		"""Get session if it is valid and not expired.

		Args:
			user (User): User model object
			session_id (int): Session row id

		Returns:
			Session or None
		"""
		try:
			session = self.select_related('user').get(
				user=user,
				id=session_id,
				is_valid=True
			)
			if session.expire_at < now():
				session.is_valid = False
				session.save()
				return None
			return session
		except Exception as e:
			return None

	def get_last_session(self, user):
		return self.filter(user=user).order_by('-created_at').first()

	def get_user(self, session_id):
		try:
			return self.get(id=session_id).user
		except Exception as e:
			return None
