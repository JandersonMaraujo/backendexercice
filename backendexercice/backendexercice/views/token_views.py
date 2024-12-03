from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response


User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to always generate a new token and invalidate the previous ones.
    """

    def post(self, request, *args, **kwargs):
        # Validate the credentials and get tokens
        response = super().post(request, *args, **kwargs)
        if response.status_code != 200:
            return response

        # Invalidate all previous tokens for the user
        user = User.objects.get(username=request.data.get("username"))
        RefreshToken.for_user(user)  # This automatically invalidates old refresh tokens

        # Return the new token pair
        return Response(
            {
                "access_token": response.data.get("access"),
                "token_type": "bearer"
            },
            status=status.HTTP_200_OK
        )



