from django.db import models
from django.contrib.auth.models import AbstractUser
from backendexercice.models.timestamps_model_base import TimestampsModel


class User(AbstractUser, TimestampsModel):
    """Class for modeling users"""

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['role']),
        ]

    class UserRoles(models.TextChoices):
        """Choices for the user roles."""

        USER = 'user'
        ADMIN = 'admin'

    role = models.CharField(
        max_length=255,
        choices=UserRoles.choices,
        null=True,
        help_text="Define whether a user is a commom or admin one.",
    )
    """Char field representing the user role."""

    def __str__(self):
        return self.username