from django.contrib import admin
from django.urls import (
    path,
    include
)

from django.conf.urls.static import static

from config.settings.base import (
    MEDIA_ROOT,
    MEDIA_URL
)

urlpatterns = [
    path('__reload__', include('django_browser_reload.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('public.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('reports/', include('reports.urls')),
    
    path('clients/', include('clients.urls')),
    path('deliveries/', include('deliveries.urls')),
    path('parcels/', include('parcels.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
