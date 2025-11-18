from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from django.conf import settings
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            raise ValueError("Password is required")
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model using UUID, email login, and links to Organization + Role.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True)
    organization = models.ForeignKey(
        "accounts.Organization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    role = models.ForeignKey(
        "accounts.Role", on_delete=models.SET_NULL, null=True, blank=True
    )
    # -----------------------
    # Django Required Fields
    # -----------------------
    is_active = models.BooleanField(default=True)  # can login?
    is_staff = models.BooleanField(default=False)  # admin-site access?

    created_at = models.DateField(auto_now_add=True)

    objects = UserManager()

    # -----------------------
    # Email is used as username
    # -----------------------

    USERNAME_FIELD = "email"     # <---- THIS MAKES EMAIL THE LOGIN FIELD

    REQUIRED_FIELDS = []         # no extra fields required for superuser

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email
