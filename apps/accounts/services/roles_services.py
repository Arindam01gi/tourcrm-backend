from apps.accounts.models import Role

def create_default_roles(organization):
    """
    Creates default roles for new organization.
    Returns a dict for easy access.
    """

    admin = Role.objects.create(
        organization=organization,
        name="Admin",
        permissions = ["*"]
    )
    manager = Role.objects.create(
        organization=organization,
        name="Manager",
        permissions= ["lead.create","lead.update","lead.view"]
    )
    executive = Role.objects.create(
        organization=organization,
        name="Executive",
        permissions=["lead.view"]
    )

    return {
        "admin": admin,
        "manager": manager,
        "executive": executive,
    }
