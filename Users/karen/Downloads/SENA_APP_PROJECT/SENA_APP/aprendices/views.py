from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Aprendiz

# Create your views here.
def home(request):
  total_aprendices = Aprendiz.objects.count()
  return render(request, 'main.html', {'total_aprendices': total_aprendices})

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    
    context = {
        'lista_aprendices': lista_aprendices,
    }
    return HttpResponse(template.render(context, request))

def detalle_aprendiz(request, id_aprendiz):
  aprendiz = Aprendiz.objects.get(id=id_aprendiz)
  template = loader.get_template('detalle_aprendiz.html')
  context = {
    'aprendiz': aprendiz,
  }
  return HttpResponse(template.render(context, request))

