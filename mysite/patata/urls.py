from django.urls import path
from . import views
urlpatterns = [
 path('', views.HomeView.as_view(), name='Home'),
 path('platform/p=<str:plataforma>', views.PlatformView.as_view(), name="Plataforma"),
 path('contact/', views.ContactView.as_view(), name='Contact'),
 path('genre/g=<str:genero>',views.GenreView.as_view(), name='Genero'),
 path('game/i=<int:id>', views.GameView.as_view(), name='Game'),
 path('registrar/', views.ContactOutputView.as_view(), name='registrar')
]
