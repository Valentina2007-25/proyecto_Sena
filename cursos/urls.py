from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    # Rutas existentes (no necesitan cambio si las vistas se mantuvieron)
    path('lista/', views.lista_cursos, name='lista_cursos'),
    path('<int:curso_id>/', views.detalle_curso, name='detalle_curso'),

    # Nuevas rutas CRUD apuntando a las Vistas Basadas en Clases
    path('crear/', views.CursoCreateView.as_view(), name='crear_curso'),
    path('<int:curso_id>/editar/', views.CursoUpdateView.as_view(), name='editar_curso'),
    path('<int:curso_id>/eliminar/', views.CursoDeleteView.as_view(), name='eliminar_curso'),
]
