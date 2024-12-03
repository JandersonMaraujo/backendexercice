from django.db import models
from django.contrib.auth import get_user_model
from backendexercice.models.timestamps_model_base import TimestampsModel


User = get_user_model()


class Report(TimestampsModel):
    """Class for modeling reports"""
    class ReportStatus(models.TextChoices):
        """Choices for the report status."""

        PENDING = 'Pending'
        COMPLETED = 'Completed'
        IN_PROGRESS = 'In progress'
        FAILED = 'Failed'
    
    title = models.CharField(max_length=128, null=False)
    status = models.CharField(
        max_length=128,
        null=False,
        choices=ReportStatus.choices
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)