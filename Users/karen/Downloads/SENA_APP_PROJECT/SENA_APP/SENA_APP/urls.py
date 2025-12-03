from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('aprendices.urls', 'aprendices'), namespace='aprendices')),
    path('instructores/', include(('instructores.urls', 'instructores'), namespace='instructores')),
]
