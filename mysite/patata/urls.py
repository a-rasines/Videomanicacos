from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('index/', views.home, name='Home'),
 path('contact/', views.contact, name='Contact')
]
