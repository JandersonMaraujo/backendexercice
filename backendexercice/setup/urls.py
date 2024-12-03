"""
URL configuration for backendexercice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from backendexercice.views.user_views import (
    CommonUserViewSet
)
from backendexercice.views.product_views import ProductViewSet
from backendexercice.views.sale_views import SaleViewSet
from backendexercice.views.report_views import ReportViewSet
from backendexercice.views.default_views import HomeView, UserView, AdminView
from backendexercice.views.token_views import CustomTokenObtainPairView


router = routers.SimpleRouter()

router.register('server-user', CommonUserViewSet, 'server-user')
router.register('product', ProductViewSet, 'product')
router.register('sale', SaleViewSet, 'sale')
router.register('report', ReportViewSet, 'report')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', HomeView.as_view()),
    path('user/', UserView.as_view()),
    path('admin/', AdminView.as_view()),
    path('admin-site/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]