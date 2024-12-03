from django.db import models
from django.contrib.auth import get_user_model
from backendexercice.models.timestamps_model_base import TimestampsModel
from backendexercice.models.product import Product


User = get_user_model()


class Sale(TimestampsModel):
    """Class for modeling sales"""
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)