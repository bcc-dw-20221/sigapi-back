from django.contrib import admin
from SIGAPI_rest.models import Curso, Aluno, Professor, Disciplina, Boletim
# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Boletim)
