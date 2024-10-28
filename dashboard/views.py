from django.shortcuts import render

def index(request):
    context = {}
    return render(
        request,
        'dashboard/pages/index.html',
        context
    )

def account(request):
    context = {}
    return render(
        request,
        'dashboard/pages/account.html',
        context
    )
