from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader
from .models import Programa
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def programas(request):
    lista_programa = Programa.objects.all()
    template = loader.get_template("lista_programa.html")
    context = {
        "lista_programa": lista_programa,
        "total_programas": lista_programa.count(),
    }
    return HttpResponse(template.render(context, request))


def detalle_programa(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    template = loader.get_template("detalle_programa.html")
    context = {
        "programa": programa,
    }
    return HttpResponse(template.render(context, request))