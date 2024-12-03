from rest_framework.viewsets import ModelViewSet
from backendexercice.models.sale import Sale
from backendexercice.serializers.sale_serializers import SaleSerializer
from backendexercice.permissions.user_permissions import HasAdminRolePermission
from rest_framework.permissions import IsAuthenticated


class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated, HasAdminRolePermission]
