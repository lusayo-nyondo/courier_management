from django.shortcuts import render

def index(request):
    context = {}
    response = render(
        request,
        'deliveries/pages/index.html',
        context
    )
    return response


