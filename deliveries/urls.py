from django.urls import (
    path
)

from .views import (
    index,
    new_delivery
)

app_name = 'deliveries'
urlpatterns = [
    path('', index, name="index"),
    path('new', new_delivery, name="new"),
]