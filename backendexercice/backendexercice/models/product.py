from django.db import models
from backendexercice.models.timestamps_model_base import TimestampsModel


class Product(TimestampsModel):
    """Class for modeling Products"""
    name = models.CharField(max_length=256, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name