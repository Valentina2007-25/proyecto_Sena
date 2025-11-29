from django.shortcuts import render
from django.http import HttpResponse
from .models import Aprendiz

# Página de inicio
def inicio(request):
    return render(request, "main.html")

# Lista de aprendices
def aprendices(request):
    lista_aprendices = Aprendiz.objects.all()
    context = {
        "lista_aprendices": lista_aprendices
    }
    return render(request, "lista_aprendices.html", context)

# Detalle de un aprendiz por ID
def detalle_aprendiz(request, id_aprendiz):
    aprendiz = Aprendiz.objects.get(id=id_aprendiz)
    context = {
        "aprendiz": aprendiz
    }
    return render(request, "detalle_aprendiz.html", context)
