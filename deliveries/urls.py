from django.urls import (
    path
)

from .views import (
    index,
)

app_name = 'deliveries'
urlpatterns = [
    path('', index, name="index"),
]