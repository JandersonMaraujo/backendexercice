from rest_framework.viewsets import ModelViewSet
from backendexercice.models.user import User
from backendexercice.serializers.user_serializers import (
    CommonUserSerializer, AdminUserSerializer,
)
from django.contrib.auth import get_user_model
from backendexercice.permissions.user_permissions import HasAdminRolePermission
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

class CommonUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CommonUserSerializer
    permission_classes = [IsAuthenticated, HasAdminRolePermission]

class AdminUserViewSet(ModelViewSet):
    queryset = User.objects.filter(role=User.UserRoles.ADMIN)
    serializer_class = AdminUserSerializer
    permission_classes = [IsAuthenticated, HasAdminRolePermission]