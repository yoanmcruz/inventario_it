from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('inventario/', include('inventario.urls')),
    path('bitacora/', include('bitacora.urls')),
    path('usuarios/', include('usuarios.urls')),
]
