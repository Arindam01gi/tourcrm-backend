from django.db import transaction, IntegrityError
from django.utils.text import slugify
from apps.accounts.models import Organization, User
from apps.accounts.services.roles_services import create_default_roles


@transaction.atomic
def create_organization_with_admin(data):
    try:
        #  Create organization
        org = Organization.objects.create(
            name=data["organization_name"],
            slug=slugify(data["organization_name"]),
            address=data.get("address")
        )

    except IntegrityError:
        raise ValueError("ORGANIZATION_ALREADY_EXISTS")

    #  Create roles
    roles = create_default_roles(org)
    admin_role = roles["admin"]

    try:
        admin_user = User.objects.create_user(
            email=data["admin_email"],
            password=data["admin_password"],
            name=data["admin_name"],
            organization=org,
            role=admin_role,
            is_staff=True
        )
    except IntegrityError:
        raise ValueError("EMAIL_ALREADY_EXISTS")

    return org, admin_user
