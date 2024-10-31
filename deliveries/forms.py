from django import forms

from .models import (
    Delivery
)

class DeliveryForm(forms.ModelForm):
    fields = '__all__'
    model = Delivery