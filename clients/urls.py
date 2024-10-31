from django.urls import (
    path
)

from .views import (
    client_list,
    client_detail,
    client_edit,
    new_client
)

app_name = 'clients'
urlpatterns = [
    path('', client_list, name="index"),
    path('new', new_client, name="new_client"),
    path('<int:client_id>/detail', client_detail, name='client_detail'),
    path('<int:client_id>/edit', client_edit, name='client_edit')
]