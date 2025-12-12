from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Aprendiz
from instructores.models import Instructor
from cursos.models import Curso
from programas.models import Programa

from .forms import AprendizForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# VISTAS BASADAS EN FUNCIONES

def detalle_aprendiz(request, id_aprendiz):
    aprendiz = Aprendiz.objects.get(id=id_aprendiz)
    return render(request, 'detalle_aprendiz.html', {'aprendiz': aprendiz})

def aprendices(request):
    """Lista todos los aprendices"""
    lista_aprendices = Aprendiz.objects.all()
    context = {
        'lista_aprendices': lista_aprendices
    }
    return render(request, 'lista_aprendices.html', context)


def home(request):
    """Página de inicio con totales"""
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_cursos = Curso.objects.count()
    total_programas = Programa.objects.count()

    context = {
        'total_aprendices': total_aprendices,
        'total_instructores': total_instructores,
        'total_cursos': total_cursos,
        'total_programas': total_programas,
    }

    return render(request, 'main.html', context)

# VISTAS BASADAS EN CLASES (CRUD)


# CREATE - APRENDIZ
class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'agregar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')

    def form_valid(self, form):
        """Mensaje de éxito al crear"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """Mensaje si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - APRENDIZ
class AprendizUpdateView(generic.UpdateView):
    """Vista para editar un aprendiz"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'editar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    pk_url_kwarg = 'aprendiz_id'

    def form_valid(self, form):
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - APRENDIZ
class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""
    model = Aprendiz
    template_name = 'eliminar_aprendiz.html'
    success_url = reverse_lazy('aprendices:lista_aprendices')
    pk_url_kwarg = 'aprendiz_id'

    def delete(self, request, *args, **kwargs):
        aprendiz = self.get_object()

        messages.success(
            request,
            f'El aprendiz {aprendiz.nombre_completo()} ha sido eliminado exitosamente.'
        )

        return super().delete(request, *args, **kwargs)
