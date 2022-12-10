from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.views import View

from .models import *

class BaseView(View):
    def eliminarVacios(arr):
        ret = {}
        arr = dict(arr)
        for v in arr:
            if (arr[v].count() != 0):
                ret[v] = arr[v]
        return ret
class ContactView(BaseView):
    vars = {
        'todasPlataformas': Plataforma.objects.all(),
        'genders': Genero.objects.all()
    }
    view:str
    def __init__(self, view='contact.html'):
        self.view = view
    def get(self, request):
        print(len(self.vars.keys()))
        return render(request, self.view, self.vars)
class HomeView(ContactView):
    def __init__(self):
        ContactView.__init__(HomeView, 'index.html')
        for key, value in[
        ('plataformas', Plataforma.objects.all()[0:4]),
        ('g', 0),
        ('featureds', Videojuego.objects.filter(featured=True)),
        ('lastests', Videojuego.objects.all()[::-1][0:8]),
        ('sections', BaseView.eliminarVacios([(i, Videojuego.objects.filter(genero=i)) for i in Genero.objects.all()]))]:
            ContactView.vars[key] = value
class GameView(View):
    def get(self,request, id):
        game = get_object_or_404(Videojuego, id=id)
        vars = {'todasPlataformas' : Plataforma.objects.all(),
                'genders': Genero.objects.all(),
                'gamePlatforms': game.plataforma.all(),
                'desc': game.description.split("\n"),
                'game': game,
                'otherGames': Videojuego.objects.filter(genero=game.genero)[0:5]
                }
        return render(request, 'single.html', vars)
class GenreView(BaseView):
    def get(self, request, genero:str):
        genero = get_object_or_404(Genero, nombre=genero)
        vars = {
            'plataformas': Plataforma.objects.all()[0:4],
            'todasPlataformas': Plataforma.objects.all(),
            'genders': Genero.objects.all(),
            'title0': "Genre",
            'title1': genero.nombre,
            'g': 1,
            'featureds': Videojuego.objects.filter(featured=True, genero=genero),
            'lastests': Videojuego.objects.all()[::-1][0:8],
            'sections': BaseView.eliminarVacios([(i, Videojuego.objects.filter(genero=genero, plataforma=i)) for i in Plataforma.objects.all()])
        }
        return render(request, 'index.html', vars)

class PlatformView(BaseView):
    def get(self,request, plataforma:str):
        plataforma = get_object_or_404(Plataforma,nombre=plataforma)
        vars = {
            'plataformas': Plataforma.objects.all()[0:4],
            'todasPlataformas': Plataforma.objects.all(),
            'genders': Genero.objects.all(),
            'title0': "Platform",
            'title1': plataforma.nombre,
            'g':0,
            'featureds': Videojuego.objects.filter(featured=True, plataforma= plataforma),
            'lastests': Videojuego.objects.all()[::-1][0:8],
            'sections': BaseView.eliminarVacios([(i, Videojuego.objects.filter(genero=i, plataforma = plataforma)) for i in Genero.objects.all()])
        }
        return render(request, 'index.html', vars)
class ContactOutputView(View):
    def post(self, request):
        try:
            open("consultas.html", "x")
            file = open("consultas.html", "w")
            text = "\
<head>\
    <style>\
        table *{\
            border: 2px solid black;\
            padding: 10px;\
        }\
    </style>\
</head>\
<body>\
    <table>\
        <tr>\
            <th>Nombre</th>\
            <th>Email</th>\
            <th>País</th>\
            <th>Asunto</th>\
            <th>Mensaje</th>\
        </tr>\
        <!-- -->\
    </table>\
</body>"
        except FileExistsError as e:
            file = open("consultas.html", "r")
            text = file.read()
            file.close()
            file = open("consultas.html", "w")
        nombre = request.POST["name"]
        email = request.POST["email"]
        country = request.POST["country"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        file.write(text.replace("<!-- -->", f"\
<tr>\
    <td>{nombre}</td>\
    <td>{email}</td>\
    <td>{country}</td>\
    <td>{subject}</td>\
    <td>{message}</td>\
</tr>\
<!-- -->"))
        file.close()
        vars={
            'todasPlataformas': Plataforma.objects.all(),
            'genders': Genero.objects.all()
        }
        return render(request, 'contactSuccess.html', vars)#HttpResponse(f"Nombre: {nombre} -- Email: {email} -- Pais de origen: {country} -- Asunto: {subject} -- Mensaje: '{message}'\n")