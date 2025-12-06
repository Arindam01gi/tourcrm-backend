from django.db import models
from django.utils import timezone
import uuid


def default_expiry():
    return timezone.now() + timezone.timedelta(hours=48)


class Invite(models.Model):
    """
    Invite model:
    Stores invitation link for employees to join an organization.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    token = models.CharField(max_length=32, unique=True, default=uuid.uuid4().hex)
    organization = models.ForeignKey(
        "accounts.Organization", on_delete=models.CASCADE, related_name="invites"
    )
    role = models.ForeignKey(
        "accounts.Role",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="invites",
    )
    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sent_invites",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # -------------------------
    # Invite expiration
    # -------------------------
    expires_at = models.DateTimeField(default=default_expiry)
    used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)
    used_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="accepted_invites",
    )

    class Meta:
        db_table = "invite"

    def __str__(self):
        return f"Invite to {self.email} for {self.organization.name}"
