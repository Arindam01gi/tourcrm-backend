from django.db import models
from apps.accounts.models.base import TenantBase


class Destination(TenantBase):
    id = models.BigAutoField(primary_key=True)
    region = models.ForeignKey(
        "itinerary.Region", 
        on_delete=models.CASCADE, 
        related_name="destinations"
    )
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "destinations"
        unique_together = ('organization', 'name')

    def __str__(self):
        return f"{self.name} ({self.region.name})"