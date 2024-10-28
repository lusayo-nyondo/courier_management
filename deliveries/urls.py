from django.urls import (
    path
)

from .views import (
    index,
    lots
)

app_name = 'carparking'
urlpatterns = [
    path('', index, name="index"),
    path('lots', lots, name='lots'),
]