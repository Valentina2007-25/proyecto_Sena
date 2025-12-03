from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.home, name='home'), # Nueva ruta para la página principal (main.html)
    path('lista/', views.aprendices, name='lista_aprendices'), # Ruta para la lista de aprendices
    path('aprendiz/<int:id_aprendiz>/', views.detalle_aprendiz, name='detalle_aprendiz'),
]
