from rest_framework import serializers

class InviteSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name= serializers.CharField(max_length=255)
    role_id = serializers.IntegerField()