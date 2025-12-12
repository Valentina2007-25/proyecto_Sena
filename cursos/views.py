from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Curso
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CursoForm

# Vistas de Lista y Detalle (Basadas en funciones, como estaban)

def lista_cursos(request):
    cursos = Curso.objects.all()
    template = loader.get_template('lista_curso.html')
    
    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
    }
    
    return HttpResponse(template.render(context, request))

def detalle_curso(request, curso_id):
    # Corregido: select_relatjed -> select_related
    curso = get_object_or_404(Curso.objects.select_related('programa', 'instructor_coordinador'), id=curso_id)
    # Las siguientes líneas podrían necesitarse dependiendo de tu template de detalle
    # aprendices_curso = curso.aprendizcurso_set.all()
    # instructores_curso = curso.instructorcurso_set.all()
    template = loader.get_template('detalle_curso.html')
    
    context = {
        'curso': curso,
        # 'aprendices_curso': aprendices_curso,
        # 'instructores_curso': instructores_curso,
    }
    
    return HttpResponse(template.render(context, request))

# VISTAS CRUD BASADAS EN CLASES

class CursoCreateView(generic.CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'crear_cursos.html'
    success_url = reverse_lazy('cursos:lista_cursos')

    def form_valid(self, form):
        messages.success(self.request, f'El curso "{form.instance.nombre}" ha sido creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)

class CursoUpdateView(generic.UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'editar_cursos.html'
    pk_url_kwarg = 'curso_id'
    success_url = reverse_lazy('cursos:lista_cursos')

    def form_valid(self, form):
        messages.success(self.request, f'El curso "{form.instance.nombre}" ha sido actualizado exitosamente.')
        return super().form_valid(form)

class CursoDeleteView(generic.DeleteView):
    model = Curso
    template_name = 'eliminar_cursos.html'
    pk_url_kwarg = 'curso_id'
    success_url = reverse_lazy('cursos:lista_cursos')

    def form_valid(self, form):
        messages.success(self.request, f'El curso "{self.get_object().nombre}" ha sido eliminado exitosamente.')
        return super().form_valid(form)