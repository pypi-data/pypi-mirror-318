import uuid
from django.db import models
from django.utils.timezone import now
from django.db import models
from ..models import User
from .managers import SessionManager


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)
    ip = models.GenericIPAddressField()
    ua = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    expire_at = models.DateTimeField()

    class Meta:
        db_table = 'axor_sessions'
        ordering = ['-created_at']

    objects = SessionManager()

    def __str__(self):
        return f"{self.pk}"
