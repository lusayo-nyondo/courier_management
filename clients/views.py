from django.shortcuts import render

def index(request):
    context = {}
    
    return render(
        request,
        'clients/pages/index.html',
        context
    )