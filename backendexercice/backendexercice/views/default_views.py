from rest_framework.views import APIView
from rest_framework.response import Response
from backendexercice.permissions.user_permissions import (
    HasUserRolePermission, HasAdminRolePermission
)
from backendexercice.models.sale import Sale
from backendexercice.models.report import Report
from backendexercice.serializers.sale_serializers import SaleSerializer
from backendexercice.serializers.report_serializers import ReportSerializer
from rest_framework.permissions import IsAuthenticated


class HomeView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        return Response(
            {
                'status': 'ok',
                'message': 'API is healthy'
            }
        )
    

class UserView(APIView):
    permission_classes = [IsAuthenticated, HasUserRolePermission]

    def get(self, request):
        user_purchases = Sale.objects.filter(user=request.user.id)
        serializer = SaleSerializer(instance=user_purchases, many=True)
        message = f'Hello, {request.user.username}'
        data = {
            "name": f'{request.user.first_name} {request.user.last_name}',
            "email": request.user.email,
            "purchases": serializer.data,
        }
        return Response(
            {
                'message': message,
                'data': data,
            }
        )


class AdminView(APIView):
    permission_classes = [IsAuthenticated, HasAdminRolePermission]

    def get(self, request):
        reports = Report.objects.filter(user=request.user.id)
        serializer = ReportSerializer(instance=reports, many=True)
        message = f'Hello, {request.user.username}'
        data = {
            "name": f'{request.user.first_name} {request.user.last_name}',
            "email": request.user.email,
            "reports": serializer.data,
        }
        return Response(
            {
                'message': message,
                'data': data,
                'user': request.user.id,
            }
        )