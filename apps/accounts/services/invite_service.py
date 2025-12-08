import uuid
from django.utils import timezone
from apps.accounts.models import Role, Invite, User


def create_invite(data, admin_user):
    email = data["email"]
    name = data["name"]
    role_id = data["role_id"]

    try:
        role = Role.objects.get(id=role_id, organization=admin_user.organization)
    except Role.DoesNotExist:
        raise ValueError("INVALID_ROLE")

    if User.objects.filter(email=email).exists():
        raise ValueError("USER_ALREADY_REGISTERED")

    token = uuid.uuid4().hex

    invite = Invite.objects.create(
        email=email,
        token=token,
        role=role,
        organization=admin_user.organization,
        created_by=admin_user,
        expires_at=timezone.now() + timezone.timedelta(hours=48),
    )

    return invite


def accept_invite(token, data):
    """
    Docstring for accept_invite

    :param token: Description
    :param data: Description

    Accepts invitation, creates user, marks invite used.
    """

    try:
        invite = Invite.objects.get(token=token, used=False)
    except Invite.DoesNotExist:
        raise ValueError("INVALID_OR_EXPIRED_INVITE")
    
    if invite.expires_at < timezone.now():
        raise ValueError("INVITE_EXPIRED")
    
    user = User.objects.create_user(
        email = invite.email,
        password = data["password"],
        name = data["name"],
        organization = invite.organization,
        role = invite.role
    )

    invite.used = True
    invite.used_by = user
    invite.used_at = timezone.now()
    invite.save()

    return user
