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
    output = "<style>*{border: 1px solid black}</style><table>"
    for e in Videojuego.objects.all():
        plataformas = ""
        for i in e.plataforma.all():
            plataformas+=f"{i.nombre}"
        output += f"<tr><td>{e.nombre}</td><td>{e.fecha_salida}</td><td>{e.pegi}</td><td>{e.comanya}</td><td>{e.url_v}</td><td>{e.genero.nombre}</td><td>{plataformas}</td></tr>"
    return HttpResponse(output + "</table>")

def gender(request):
    output = "<style>*{border: 1px solid black}</style><table>"
    for e in Genero.objects.all():
        output+= f"<tr><td>{e.nombre}</td></tr>"
    return HttpResponse(output + "</table>")

def platform(request):
    output = "<style>*{border: 1px solid black}</style><table>"
    for e in Plataforma.objects.all():
        output += f"<tr><td>{e.nombre}</td><td>{e.owner}</td><td>{e.url_p}</td></tr>"
    return HttpResponse(output + "</table>")
