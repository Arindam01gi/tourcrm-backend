from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from apps.accounts.serializers.invite_serializers import (
    InviteSerializer,
    AcceptInviteSerializer,
)
from apps.accounts.services.invite_service import create_invite, accept_invite


class InviteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InviteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            invite = create_invite(serializer.validated_data, request.user)
        except ValueError as e:
            code = str(e)

            if code == "INVALID_ROLE":
                return Response(
                    {
                        "error": "INVALID_ROLE",
                        "message": "Role does not belong to your organization.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if code == "USERA_ALREADY_EXIST":
                return Response(
                    {
                        "error": "USER_ALREADY_EXIST",
                        "message": "User with this email already exists.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        invite_link = (
            f"http://localhost:8000/api/accounts/accept-invite/{invite.token}/"
        )

        return Response(
            {"message": "Invite created successfully.", "invite_link": invite_link},
            status=status.HTTP_201_CREATED,
        )


class AcceptInviteView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, token):
        serializer = AcceptInviteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"error": "VALIDATION_ERROR", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = accept_invite(token, serializer.validated_data)
        except ValueError as e:
            code = str(e)

            if code == "INVALID_OR_EXPIRED_INVITE":
                return Response(
                    {
                        "error": "INVALID_INVITATION",
                        "message": "Invite link is invalid or already used.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if code == "INVITE_EXPIRED":
                return Response(
                    {
                        "error": "EXPIRED_INVITATION",
                        "message": "Invitation has been expired",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        refresh = RefreshToken.for_user(user)

        response_data = {
            "message": "Invite accepted successfully. Welcome!",
            "token": {"access": str(refresh.access_token), "refresh": str(refresh)},
            "user": {
                "id": str(user.id),
                "name": user.name,
                "email": user.email,
                "role": user.role.name,
                "organization": {
                    "id": str(user.organization.id),
                    "name": user.organization.name,
                    "slug": user.organization.slug,
                },
            },
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
