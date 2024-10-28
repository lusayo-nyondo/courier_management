from django.http import (
    BadHeaderError,
    HttpResponseRedirect
)

from django.urls import reverse

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
    if request.method == 'GET':
        client = ClientForm()
    elif request.method == "POST":
        print(request.POST)
        client = ClientForm(request.POST)
        
        is_valid = client.is_valid()
        
        if is_valid:
            client.save()
            return HttpResponseRedirect(
                reverse('clients:index')
            )
    else:
        raise BadHeaderError('Unsupported HTTP method.')
    
    context = {
        'client': client
    }
    
    return render(
        request,
        'clients/pages/add_client.html',
        context
    )
    
def view_client(request, client_id):
    client = Client.objects.get(
        id=client_id
    )
    
    client_form = ClientForm(
        instance=client
    )
    
    context = {
        'client': client_form
    }
    
    return render(
        request,
        'clients/pages/single_client.html',
        context
    )