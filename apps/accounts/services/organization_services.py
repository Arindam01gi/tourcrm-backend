from django.db import transaction
from django.utils.text import slugify
from apps.accounts.models import Role, Organization, User
from apps.accounts.services.roles_services import create_default_roles


@transaction.atomic
def create_organization_with_admin(data):
    """
    Handles the full signup flow:
    1. Create organization
    2. Create default roles
    3. Create admin user
    """
    # Create Organization
    org = Organization.objects.create(
        name = data["organization_name"],
        slug = slugify(data["organization_name"]),
        address = data.get("address")
    )

    # Create Default Roles
    roles = create_default_roles(org)
    admin_role = roles["admin"]

    # Create Admin User
    admin_user = User.objects.create_user(
        email=data["admin_email"],
        password=data["admin_password"],
        name=data["admin_name"],
        organization=org,
        role=admin_role,
        is_staff=True
    )
    return org, admin_user
