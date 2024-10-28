from django.shortcuts import render

def index(request):
    context = {}
    
    return render(
        request,
        'reports/pages/index.html',
        context
    )