from django.urls import (
    path
)

from .views import (
    index,
    add_client
)

app_name = 'clients'
urlpatterns = [
    path('', index, name="index"),
    path('add_client', add_client, name="add_client")
]