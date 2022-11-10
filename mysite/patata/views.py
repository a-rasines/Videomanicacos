from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *


def index(request):
 return HttpResponse("Hello, world!")

def home(request):
    vars = {
        'plataformas' : Plataforma.objects.all()[0:4],
        'featureds': Videojuego.objects.all()[0:8],
        'sections' : [Videojuego.objects.filter(genero=i) for i in Genero.objects.all()]
    }
    return render(request, 'static/index.html', vars)

def contact(request):
    return render(request, 'static/contact.html', {})


def games(request):
    output = ""
    for e in Videojuego.objects.all():
        plataformas = ""
        for i in e.plataforma.all():
            plataformas+=f"{i.nombre}"
        output += f"{e.nombre},{e.fecha_salida},{e.pegi},{e.comanya},{e.url_v},{e.genero.nombre},{plataformas}\n"  
    return HttpResponse(output)

def gender(request):
    output = ""
    for e in Genero.objects.all():
        output+= f"{e.nombre}\n"
    return HttpResponse(output)

def platform(request):
    output = ""
    for e in Plataforma.objects.all():
        output+= f"{e.nombre},{e.owner},{e.url_p}\n"
    return HttpResponse(output)
