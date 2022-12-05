from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name='Home'),
 path('platform/<str:plataforma>', views.platform, name="Plataforma"),
 path('contact/', views.contact, name='Contact'),
 path('games/',views.games, name='Juegos'),
 path('genre/<str:genero>',views.gender, name='Genero'),
 path('game/<int:id>', views.game, name="Game")
 #path('platform/',views.platform, name='Plataforma')
]
