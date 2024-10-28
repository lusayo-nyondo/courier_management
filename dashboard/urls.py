from django.urls import path

from .views import (
    index,
    account
)

app_name = 'dashboard'
urlpatterns = [
    path('', index, name='index'),
    path('account', account, name='account'),
]