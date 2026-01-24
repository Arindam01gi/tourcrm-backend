from django.db import models
from apps.accounts.models.base import TenantBase

class Season(TenantBase):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    # If a date falls into two seasons, the higher priority one is used.
    priority = models.IntegerField(default=0)

    class Meta:
        db_table = "seasons"
        # Organization shouldn't have two seasons with the same name
        unique_together = ('organization', 'name')

    def __str__(self):
        """
        Return a human-readable representation of the season including its start and end dates.
        
        Returns:
            str: String in the format "<name> (<start_date> to <end_date>)".
        """
        return f"{self.name} ({self.start_date} to {self.end_date})"