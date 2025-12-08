from rest_framework import serializers

class InviteSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name= serializers.CharField(max_length=255)
    role_id = serializers.IntegerField()


class AcceptInviteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only = True, min_length=6)