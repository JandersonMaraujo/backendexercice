from rest_framework import serializers
from backendexercice.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id','created_at', 'updated_at']

