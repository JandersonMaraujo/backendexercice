from rest_framework.viewsets import ModelViewSet
from backendexercice.models.report import Report
from backendexercice.serializers.report_serializers import ReportSerializer
from backendexercice.permissions.user_permissions import HasAdminRolePermission
from rest_framework.permissions import IsAuthenticated


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, HasAdminRolePermission]
