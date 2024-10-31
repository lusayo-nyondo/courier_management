from django.db import models
import os

class Parcel(models.Model):
    name: models.CharField = models.CharField(
        max_length=255
    )
    description: models.TextField = models.TextField()
    weight: models.FloatField = models.FloatField()
    created_on: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_on: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.name

def _get_parcel_image_upload_path(self):
    return os.path.join(
        'parcels',
        self.parcel.id
    )
"""
class ParcelImage(models.Model):
    parcel: models.ForeignKey = models.ForeignKey(
        Parcel,
        on_delete=models.CASCADE
    )
    image: models.ImageField = models.ImageField(
        upload_to=_get_parcel_image_upload_path
    )
    created_on: models.DateTimeField = models.DateTimeField(
        auto_created=True
    )
    updated_on: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return f"{self.parcel}/{self.id}"""