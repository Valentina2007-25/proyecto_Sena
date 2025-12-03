from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Instructor

def instructores(request):
    lista_instructores = Instructor.objects.all().values()
    template = loader.get_template('lista_instructores.html')
    
    context = {
        'lista_instructores': lista_instructores,
    }
    return HttpResponse(template.render(context, request))

def detalle_instructor(request, id_instructor):
  instructor = Instructor.objects.get(id=id_instructor)
  template = loader.get_template('detalle_instructores.html')
  context = {
    'instructor':instructor ,
  }
  return HttpResponse(template.render(context, request))

def home(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())