from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name='Home'),
 path('platform/p=<str:plataforma>', views.platform, name="Plataforma"),
 path('contact/', views.contact, name='Contact'),
 path('games/',views.games, name='Juegos'),
 path('genre/g=<str:genero>',views.gender, name='Genero'),
 path('game/i=<int:id>', views.game, name="Game"),
]
