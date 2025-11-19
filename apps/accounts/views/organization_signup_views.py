from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.accounts.serializers.organization_signup_serializer import (
    OrganizationSignupSerializer,
)
from apps.accounts.services.organization_services import create_organization_with_admin


class OrganizationSignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrganizationSignupSerializer(data=request.data)

        # Validate input
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        org, admin_user = create_organization_with_admin(serializer.validated_data)

        # Generate JWT token
        refresh = RefreshToken.for_user(admin_user)

        response_data = {
            "organization": {
                "id": str(org.id),
                "name": org.name,
                "slug": org.slug,
            },
            "user": {
                "id": str(admin_user.id),
                "email": admin_user.email,
                "name": admin_user.name,
                "role": admin_user.role.name,
            },
            "token": {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
