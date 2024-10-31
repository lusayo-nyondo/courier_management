from django.shortcuts import render

from django.urls import (
    reverse
)

from django.http import (
    HttpResponseRedirect
)

from .models import (
    Delivery
)

from .forms import (
    DeliveryForm
)

def index(request):
    object_list = Delivery.objects.all()
    
    context = {
        'object_list': object_list
    }
    
    return render(
        request,
        'deliveries/pages/index.html',
        context
    )
    
def new_delivery(request):
    if request.method == 'GET':
        form = DeliveryForm()
    elif request.method == 'POST':
        form = DeliveryForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(
                reverse('deliveries:index')
            )
        
    context = {
        'form': form
    }
    
    return render(
        request,
        'deliveries/new.html',
        context
    )