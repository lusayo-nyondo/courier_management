from django.shortcuts import render

def index(request):
    context = {}
    
    return render(
        request,
        'parcels/pages/index.html',
        context
    )
