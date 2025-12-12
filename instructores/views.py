from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Instructor
from .forms import InstructorForm

# Vistas basadas en función (modernizadas)

def instructores(request):
    """Lista todos los instructores."""
    lista_instructores = Instructor.objects.all()
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return render(request, 'lista_instructores.html', context)

def detalle_instructor(request, pk):
    """Muestra los detalles de un instructor específico."""
    instructor = get_object_or_404(Instructor, pk=pk)
    context = {
        'instructor': instructor,
    }
    return render(request, 'detalle_instructor.html', context)

# Vistas Basadas en Clases (Corregidas)

class InstructorCreateView(CreateView):
    """Vista para crear un nuevo instructor."""
    model = Instructor
    form_class = InstructorForm
    template_name = 'crear_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorUpdateView(UpdateView):
    """Vista para actualizar un instructor existente."""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    # No se necesita pk_url_kwarg porque la URL ahora usa 'pk', que es el valor por defecto.
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorDeleteView(DeleteView):
    """Vista para eliminar un instructor."""
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    # No se necesita pk_url_kwarg porque la URL ahora usa 'pk'.
    
    def form_valid(self, form):
        # Usamos form_valid para añadir el mensaje de éxito antes de que se elimine el objeto.
        messages.success(
            self.request,
            f'El instructor {self.get_object().nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().form_valid(form)