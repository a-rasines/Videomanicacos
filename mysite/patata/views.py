from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *


def index(request):
 return HttpResponse("Hello, world!")

def home(request):
    vars = {
        'plataformas' : Plataforma.objects.all()[0:4],
    }
    return render(request, 'static/index.html', vars)

def contact(request):
    return render(request, 'static/contact.html', {})