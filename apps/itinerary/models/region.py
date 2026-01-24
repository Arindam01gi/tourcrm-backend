from django.db import models
from apps.accounts.models.base import TenantBase

class Region(TenantBase):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    # Store rich text or bullet points for the itinerary PDF
    inclusions = models.TextField(blank=True, null=True)
    exclusions = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "regions"
        unique_together = ('organization', 'name')

    def __str__(self):
        """
        Provide the region's name as the object's string representation.
        
        Returns:
            str: The region's name.
        """
        return self.name