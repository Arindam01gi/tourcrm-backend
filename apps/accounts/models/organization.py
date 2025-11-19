from django.db import models
import uuid


class Organization(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=255,blank=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'organization'

    def __str__(self):
        return self.name