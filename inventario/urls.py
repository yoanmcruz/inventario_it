from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipos, name='lista_equipos'),
    path('equipo/<int:pk>/', views.detalle_equipo, name='detalle_equipo'),
    path('agregar/', views.agregar_equipo, name='agregar_equipo'),
    path('modificar/<int:pk>/', views.modificar_equipo, name='modificar_equipo'),
    path('eliminar/<int:pk>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('exportar/excel/', views.exportar_equipos_excel, name='exportar_equipos_excel'),
    path('exportar/pdf/', views.exportar_equipos_pdf, name='exportar_equipos_pdf'),
]
