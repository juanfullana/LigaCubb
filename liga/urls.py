from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para la página principal
    path('prueba/', views.prueba, name='prueba'),  # URL de prueba
]