from django.urls import path, include
from SIGAPI_rest import views
from rest_framework import routers
from SIGAPI_rest.viewsets import (CursoViewSet, UserViewSet, AlunoViewSet, EgressoViewSet, PaisViewSet, ProfessorViewSet, DisciplinaViewSet, BoletimViewSet)
router = routers.DefaultRouter()
router.register(r"cursos",CursoViewSet)
router.register(r"users",UserViewSet)
router.register(r"aluno", AlunoViewSet)
router.register(r"Egresso", EgressoViewSet)
router.register(r"Pais de alunos", PaisViewSet)
router.register(r"professor", ProfessorViewSet)
router.register(r"disciplina", DisciplinaViewSet)
router.register(r"boletim", BoletimViewSet)
urlpatterns = [
    path("", views.get_Cursos, name="get_Curso"),
    path("add/", views.post_Curso, name="post_Curso"),
    path("get/<curso_id>/", views.get_Curso, name="get_Curso"),
    path("remove/<curso_id>/", views.delete_Curso, name="delete_Curso"),
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
