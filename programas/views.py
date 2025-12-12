from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import Programa
from .forms import ProgramaForm

def main(request):
    # Suponiendo que main.html está en la carpeta de templates de 'aprendices'
    return render(request, "main.html")

def programas(request):
    lista_programa = Programa.objects.all()
    context = {
        "lista_programa": lista_programa,
        "total_programas": lista_programa.count(),
    }
    return render(request, "lista_programa.html", context)


def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    context = {
        "programa": programa,
    }
    return render(request, "detalle_programa.html", context)

# VISTAS CRUD BASADAS EN CLASES

class ProgramaCreateView(generic.CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'crear_programa.html'
    success_url = reverse_lazy('programa:lista_programa')

    def form_valid(self, form):
        messages.success(self.request, f'El programa "{form.instance.nombre}" ha sido creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)

class ProgramaUpdateView(generic.UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    pk_url_kwarg = 'programa_id'
    success_url = reverse_lazy('programa:lista_programa')

    def form_valid(self, form):
        messages.success(self.request, f'El programa "{form.instance.nombre}" ha sido actualizado exitosamente.')
        return super().form_valid(form)

class ProgramaDeleteView(generic.DeleteView):
    model = Programa
    template_name = 'eliminar_programa.html'
    pk_url_kwarg = 'programa_id'
    success_url = reverse_lazy('programa:lista_programa')

    def form_valid(self, form):
        messages.success(self.request, f'El programa "{self.get_object().nombre}" ha sido eliminado exitosamente.')
        return super().form_valid(form)