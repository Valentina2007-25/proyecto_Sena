from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aprendices.urls')),
    path('aprendices/', include('aprendices.urls')),
    path("instructores/",include('instructores.urls')),
    path("programas/",include('programas.urls'))
]