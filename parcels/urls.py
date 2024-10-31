from django.urls import (
    path
)

from .views import (
    index,
    add_parcel
)

app_name = 'parcels'
urlpatterns = [
    path('', index, name='index'),
    path('add_parcel', add_parcel, name='add_parcel')
]
