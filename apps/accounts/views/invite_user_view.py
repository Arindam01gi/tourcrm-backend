from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.accounts.serializers.invite_serializers import InviteSerializer
from apps.accounts.services.invite_service import create_invite


class InviteView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self,request):
        serializer = InviteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        try:
            invite = create_invite(serializer.validated_data,request.user)
        except ValueError as e:
            code = str(e)

            if code == "INVALID_ROLE":
                return Response({
                    "error": "INVALID_ROLE",
                    "message": "Role does not belong to your organization."
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if code == "USERA_ALREADY_EXIST":
                return Response({
                    "error" : "USER_ALREADY_EXIST",
                    "message" : "User with this email already exists."
                },status=status.HTTP_400_BAD_REQUEST)
            
        invite_link = f"http://localhost:8000/api/accounts/accept-invite/{invite.token}/"

        return Response({
            "message": "Invite created successfully.",
            "invite_link": invite_link
        }, status=status.HTTP_201_CREATED)