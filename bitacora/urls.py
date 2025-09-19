from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:pk>/', views.agregar_registro_bitacora, name='agregar_registro_bitacora'),
    path('auditoria/', views.lista_auditoria, name='lista_auditoria'),
]