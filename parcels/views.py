from django.shortcuts import render

from .forms import (
    ParcelForm,
    ParcelFormSet
)

def index(request):
    formset = ParcelFormSet()
    
    context = {
        formset: formset
    }
    
    return render(
        request,
        'parcels/pages/index.html',
        context
    )

def add_parcel(request):
    form = ParcelForm()
    
    context = {
        'form': form
    }
    
    return render(
        request,
        'parcels/pages/add_parcel.html',
        context
    )