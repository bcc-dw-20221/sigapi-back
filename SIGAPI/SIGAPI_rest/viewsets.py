from multiprocessing.connection import wait
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions

from rest_framework import viewsets
from SIGAPI_rest.models import Curso, Aluno, Professor, Disciplina, Boletim
from django.contrib.auth import get_user_model
from SIGAPI_rest.serializer import (CursoSerializer, 
                                    CreateUserSerializer, 
                                    CreateAlunoSerializer, 
                                    CreateProfessorSerializer,
                                    CreateDisciplinasSerializer,
                                    CreateBoletimSerializer)

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = CreateUserSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Aluno.objects.all()
    serializer_class = CreateAlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Professor.objects.all()
    serializer_class = CreateProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Disciplina.objects.all()
    serializer_class = CreateDisciplinasSerializer

class BoletimViewSet(viewsets.ModelViewSet):
    queryset = Boletim.objects.all()
    serializer_class = CreateBoletimSerializer

