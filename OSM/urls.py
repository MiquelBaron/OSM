from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.nuevo, name='nuevo'),
    path('lista/', views.lista, name='lista'),
    path('modificar/<int:id>/', views.modificar, name='modificar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('marcar/<int:id>/', views.marcar, name='marcar'),
    path('cocina/', views.cocina, name='cocina'),
    path('progreso/<int:id>', views.progreso, name='progreso'),
    path('listo/<int:id>', views.listo, name='listo'),
    path('entregado/', views.entregado, name='entregado'),
]