from django.db import models

from clients.models import (
    Client
)

from parcels.models import (
    Parcel
)

class Delivery(models.Model):
    class Meta:
        verbose_name_plural = 'deliveries'
    
    STATUSES = (
        ('awaiting_dropoff', 'Awaiting Dropoff'),
        ('awaiting_pickup', 'Awaiting Pickup')
    )
    from_address: models.TextField = models.TextField()
    to_address: models.TextField = models.TextField()
    sender: models.ForeignKey = models.ForeignKey(
        Client,
        on_delete=models.DO_NOTHING,
    )
    receiver: models.ForeignKey = models.ForeignKey(
        Client,
        on_delete=models.DO_NOTHING
    )
    parcel: models.ForeignKey = models.ForeignKey(
        Parcel,
        on_delete=models.DO_NOTHING
    )
    
    created_on: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_on: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )
    expected_delivery_date: models.DateTimeField = models.DateTimeField()
    status: models.CharField = models.CharField(
        max_length=255,
        choices=STATUSES
    )
    
    def __str__(self):
        return f'{ self.sender } - { self.parcel } - { self.expected_delivery_date }'
    
class DeliveryTrackingNote(models.Model):
    delivery: models.ForeignKey = models.ForeignKey(
        Delivery,
        on_delete=models.DO_NOTHING
    )
    note: models.TextField = models.TextField()
    created_on: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )
    updated_on: models.DateTimeField = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return f"{ self.created_on } - { self.delivery }"
    
