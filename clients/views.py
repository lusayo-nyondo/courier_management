from django.shortcuts import render

from .models import (
    Client
)

from .forms import (
    ClientForm
)

def index(request):
    clients = Client.objects.all()
    
    context = {
        'clients': clients
    }
    
    return render(
        request,
        'clients/pages/index.html',
        context
    )

def add_client(request):
    client = ClientForm()
    
    context = {
        'client': client
    }
    
    return render(
        request,
        'clients/pages/add_client.html',
        context
    )