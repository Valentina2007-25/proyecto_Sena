from django.contrib import admin
from .models import Curso
from .models import InstructorCurso
from .models import AprendizCurso
admin.site.register(InstructorCurso)
admin.site.register(AprendizCurso)
admin.site.register(Curso)
# Register your models here.
