from django.db.models import DecimalField
from django.db import models
from apps.accounts.models.base import TenantBase


class Car(TenantBase):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False,blank=False)
    capacity = models.IntegerField(null=False,blank=False)

    class Meta:
        db_table = "car"
        unique_together = ('organization', 'name')

    def __str__(self):
        """
        Human-readable representation of the car including its name and seating capacity.
        
        Returns:
            str: The car's display string in the format "<name> (<capacity> seats)".
        """
        return f"{self.name} ({self.capacity} seats)"

class CarPricing(TenantBase):
    id = models.BigAutoField(primary_key=True)
    car = models.ForeignKey(
        "itinerary.Car",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    season = models.ForeignKey(
        "itinerary.Season",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    price = DecimalField(
        max_digits=10, decimal_places=2
    )
    region = models.ForeignKey(
        "itinerary.Region",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "car_pricing"
        unique_together = ('organization', 'car', 'season', 'region')
    
    def __str__(self):
        """
        Provide a human-readable representation of the CarPricing instance.
        
        Returns:
            str: A string formatted as "<car.name> - <region.name> - <price>".
        """
        return f"{self.car.name} - {self.region.name} - {self.price}"