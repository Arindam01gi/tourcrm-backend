import uuid
from django.utils import timezone
from apps.accounts.models import Role,Invite,User


def create_invite(data,admin_user):
    email= data["email"]
    name= data["name"]
    role_id = data["role_id"]

    try:
        role = Role.objects.get(id=role_id,organization=admin_user.organization)
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
        expires_at=timezone.now()+timezone.timedelta(hours=48)
    )

    return invite