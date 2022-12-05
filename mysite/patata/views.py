from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import *

def home(request):
    vars = {
        'plataformas' : Plataforma.objects.all()[0:4],
        'todasPlataformas' : Plataforma.objects.all(),
        'genders' : Genero.objects.all(),
        'g': 0,
        'featureds' : Videojuego.objects.filter(featured=True),
        'lastests': Videojuego.objects.all()[::-1][0:8],
        'sections' : eliminarVacios([(i, Videojuego.objects.filter(genero=i)) for i in Genero.objects.all()])
    }
    return render(request, 'index.html', vars)

def contact(request):
    vars = {
        'plataformas' : Plataforma.objects.all(),
        'generos': Genero.objects.all()
    }
    return render(request, 'contact.html', vars)

def games(request):
    output = "<style>*{border: 1px solid black}</style><table>"
    for e in Videojuego.objects.all():
        plataformas = ""
        for i in e.plataforma.all():
            plataformas+=f"{i.nombre}, "
        output += f"<tr><td>{e.nombre}</td><td>{e.fecha_salida}</td><td>{e.pegi}</td><td>{e.comanya}</td><td>{e.url_v}</td><td>{e.genero.nombre}</td><td>{plataformas}</td></tr>"
    return HttpResponse(output + "</table>")

def game(request, id):
    game = get_object_or_404(Videojuego, id=id)
    vars = {'genres' : Genero.objects.all(),
            'platforms': Plataforma.objects.all(),
            'gamePlatforms': game.plataforma.all(),
            'desc': game.description.split("\n"),
            'game': game,
            'otherGames': Videojuego.objects.filter(genero=game.genero)[0:5]
            }
    return render(request, 'single.html', vars)
def gender(request, genero:str):
    genero = get_object_or_404(Genero, nombre=genero)
    vars = {
        'plataformas': Plataforma.objects.all()[0:4],
        'todasPlataformas': Plataforma.objects.all(),
        'genders': Genero.objects.all(),
        'g': 1,
        'featureds': Videojuego.objects.filter(featured=True, genero=genero),
        'lastests': Videojuego.objects.all()[::-1][0:8],
        'sections': eliminarVacios([(i, Videojuego.objects.filter(genero=genero, plataforma=i)) for i in Plataforma.objects.all()])
    }
    return render(request, 'index.html', vars)

def platform(request, plataforma:str):
    plataforma = get_object_or_404(Plataforma,nombre=plataforma)
    vars = {
        'plataformas': Plataforma.objects.all()[0:4],
        'todasPlataformas': Plataforma.objects.all(),
        'genders': Genero.objects.all(),
        'g':0,
        'featureds': Videojuego.objects.filter(featured=True, plataforma= plataforma),
        'lastests': Videojuego.objects.all()[::-1][0:8],
        'sections': eliminarVacios([(i, Videojuego.objects.filter(genero=i, plataforma = plataforma)) for i in Genero.objects.all()])
    }
    return render(request, 'index.html', vars)
    '''output = "<style>*{border: 1px solid black}</style><table>"
    for e in Plataforma.objects.all():
        output += f"<tr><td>{e.nombre}</td><td>{e.owner}</td><td>{e.url_p}</td></tr>"
    return HttpResponse(output + "</table>")'''

def eliminarVacios(arr):
    ret = {}
    arr = dict(arr)
    for v in arr:
        if(arr[v].count() != 0):
            ret[v] = arr[v]
    return ret