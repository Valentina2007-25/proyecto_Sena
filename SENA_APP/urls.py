from django.contrib import admin
from django.urls import path,include
from aprendices import views as aprendices_views # Importar views de aprendices

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', aprendices_views.home, name='home'), # Página de inicio
    path('aprendices/', include('aprendices.urls')),
    path("instructores/",include('instructores.urls')),
    path("programas/",include('programas.urls')),
    path("cursos/",include('cursos.urls'))
]

# Personalización del panel administrativo
admin.site.site_header = "Panel Administrativo SENA"
admin.site.site_title = "SENA APP"
admin.site.index_title = "Gestión de Aprendices"