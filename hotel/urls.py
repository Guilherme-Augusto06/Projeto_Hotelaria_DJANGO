from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),         # Inclui as urls do app blog
    path('quartos', views.quartos, name="quartos"), # Inclui as urls do app blog
    path('reservas', views.reservas, name='reservas')
]