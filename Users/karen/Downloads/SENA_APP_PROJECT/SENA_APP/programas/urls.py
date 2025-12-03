from django.urls import path
from . import views

app_name = 'programa'

urlpatterns = [
    path('', views.main, name='home'), # Nueva ruta para la página principal (main.html)
    path('lista/', views.programas, name='lista_programa'), # Ruta para la lista de aprendices
    path('programa/<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
]
