from django.urls import path
from . import views

app_name = 'programa'

urlpatterns = [
    path('', views.main, name='home'),
    path('lista/', views.programas, name='lista_programa'),
    path('crear/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
    path('<int:programa_id>/editar/', views.ProgramaUpdateView.as_view(), name='editar_programa'),
    path('<int:programa_id>/eliminar/', views.ProgramaDeleteView.as_view(), name='eliminar_programa'),
]
