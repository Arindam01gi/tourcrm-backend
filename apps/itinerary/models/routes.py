from django.db import models
from apps.accounts.models.base import TenantBase

class Route(TenantBase):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    start_point = models.ForeignKey(
        "Destination", 
        on_delete=models.CASCADE, 
        related_name="routes_starting_here"
    )
    end_point = models.ForeignKey(
        "Destination", 
        on_delete=models.CASCADE, 
        related_name="routes_ending_here"
    )
    
    distance = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "routes"
        unique_together = ('organization', 'start_point', 'end_point')

    def __str__(self):
        """
        Return a human-readable label for the route combining the start and end destination names.
        
        Returns:
            str: A string in the form "<start_point.name> to <end_point.name>".
        """
        return f"{self.start_point.name} to {self.end_point.name}"