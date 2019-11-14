from django.urls import path
from .views import agregar_evento_global, crear_conversacion_global, conversaciones_globales, ver_conversacion
urlpatterns = [
    path('agregar_evento_global/',agregar_evento_global, name = 'agregar_evento_global'),
    path('crear_conversacion_global/',crear_conversacion_global, name = 'crear_conversacion_global'),
    path('conversaciones_globales/',conversaciones_globales, name = 'conversaciones_globales'),
    path('ver_conversacion/',ver_conversacion, name = 'ver_conversacion')
]