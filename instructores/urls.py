from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    
    path('', views.instructores, name='lista_instructores'),
    
    path('<int:pk>/', views.detalle_instructor, name='detalle_instructor'),
   
    path('crear/', views.InstructorCreateView.as_view(), name='crear_instructor'),

    path('<int:pk>/editar/', views.InstructorUpdateView.as_view(), name='editar_instructor'),

    path('<int:pk>/eliminar/', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
]

