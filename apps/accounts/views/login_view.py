from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.serializers.login_serializers import LoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"errors": "VALIDATION ERROR", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response(
                {
                    "errors": "INVALID_CREDENTIALS",
                    "message": "Email or password is incorrect.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if not user.organization:
            return Response(
                {
                    "error": "NO_ORGANIZATION",
                    "message": "User is not associcated with any organizations",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Generate tokens
        refresh = RefreshToken.for_user(user)

        response_data = {
            "token": {"access": str(refresh.access_token), "refresh": str(refresh)},
            "user": {
                "id": str(user.id),
                "name": user.name,
                "email": user.email,
                "role": user.role.name if user.role else None,
                "organization": {
                    "id": str(user.organization.id),
                    "name": user.organization.name,
                    "slug": user.organization.slug,
                },
            },
        }

        return Response(response_data, status=status.HTTP_200_OK)
