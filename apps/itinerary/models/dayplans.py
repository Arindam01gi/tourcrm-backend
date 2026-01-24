from django.db import models
from apps.accounts.models.base import TenantBase

class DayPlan(TenantBase):
    id = models.BigAutoField(primary_key=True)
    destination = models.ForeignKey(
        "Destination", 
        on_delete=models.CASCADE, 
        related_name="day_plans"
    )
    title = models.CharField(max_length=255) # e.g., "Old Delhi Sightseeing"
    description = models.TextField()

    class Meta:
        db_table = "day_plans"

    def __str__(self):
        """
        Return a human-readable representation combining the day plan's title and its destination name.
        
        Returns:
            str: A string in the format "<title> - <destination.name>".
        """
        return f"{self.title} - {self.destination.name}"