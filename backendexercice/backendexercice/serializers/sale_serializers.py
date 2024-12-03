from rest_framework import serializers
from backendexercice.models.sale import Sale
from backendexercice.serializers.product_serializers import ProductSerializer


class SaleSerializer(serializers.ModelSerializer):
    item = ProductSerializer()
    class Meta:
        model = Sale
        fields = ['id', 'item']

