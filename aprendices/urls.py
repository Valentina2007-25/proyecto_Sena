from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.aprendices, name='lista_aprendices'),
    path('crear/', views.AprendizCreateView.as_view(), name='crear_aprendiz'),
    path('<int:id_aprendiz>/', views.detalle_aprendiz, name='detalle_aprendiz'),
    path('<int:aprendiz_id>/editar/', views.AprendizUpdateView.as_view(), name='editar_aprendiz'),
    path('<int:aprendiz_id>/eliminar/', views.AprendizDeleteView.as_view(), name='eliminar_aprendiz'),
]
