from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView
)

from .models import (
    Delivery
)

class ListDeliveriesView(ListView):
    model = Delivery

def index(request):
    context = {}
    response = render(
        request,
        'deliveries/pages/index.html',
        context
    )
    return response


