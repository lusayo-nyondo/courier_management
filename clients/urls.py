from django.urls import (
    path
)

from .views import (
    index,
    add_client,
    view_client
)

app_name = 'clients'
urlpatterns = [
    path('', index, name="index"),
    path('add_client', add_client, name="add_client"),
    path('view_client/<int:client_id>', view_client, name='view_client'),
]