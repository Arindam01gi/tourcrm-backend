from django.db import models

class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=512)
    note = models.TextField()
    organization = models.ForeignKey(
        "accounts.Organization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='region'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "region"
