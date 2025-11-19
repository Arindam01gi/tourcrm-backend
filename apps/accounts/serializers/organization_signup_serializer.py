from rest_framework import serializers


class OrganizationSignupSerializer(serializers.Serializer):
    """
    Validates the signup data passed to the signup API.
    Responsible only for validation, not saving.
    """
    organization_name = serializers.CharField(max_length=255)
    admin_name = serializers.CharField(max_length=255)
    admin_email = serializers.EmailField()
    admin_password = serializers.CharField(write_only=True, min_length=6)