from django import forms

from .models import (
    Parcel
)

class ParcelForm(forms.ModelForm):
    
    class Meta:
        fields = '__all__'
        model = Parcel