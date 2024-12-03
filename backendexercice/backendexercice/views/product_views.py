from rest_framework.viewsets import ModelViewSet
from backendexercice.models.product import Product
from backendexercice.serializers.product_serializers import ProductSerializer
from backendexercice.permissions.user_permissions import HasAdminRolePermission
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, HasAdminRolePermission]
