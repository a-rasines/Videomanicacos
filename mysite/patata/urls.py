from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name='Home'),
 path('contact/', views.contact, name='Contact'),
 path('games/',views.games, name='Juegos'),
 path('genres/',views.gender, name='Genero'),
 path('platform/',views.platform, name='Plataforma')
]
