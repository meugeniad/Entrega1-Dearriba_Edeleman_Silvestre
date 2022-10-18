from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('', include('seguridad.urls')),
    path('admin/', admin.site.urls),
]
