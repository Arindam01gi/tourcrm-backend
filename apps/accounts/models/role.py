from django.db import models
import uuid


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    organization = models.ForeignKey(
        "accounts.Organization",
        on_delete=models.CASCADE,
        related_name="roles"
    )

    name = models.CharField(max_length=100)
    permissions = models.JSONField(default=list)

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.name
