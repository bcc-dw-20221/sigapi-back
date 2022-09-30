from multiprocessing.connection import wait
from rest_framework import viewsets
from SIGAPI_rest.models import Curso, Aluno, Egresso, Pais_aluno, Professor, Disciplina, Boletim
from django.contrib.auth import get_user_model
from SIGAPI_rest.serializer import (CursoSerializer, 
                                    CreateUserSerializer, 
                                    CreateAlunoSerializer, 
                                    CreateEgressoSerializer, 
                                    CreatePaisSerializer, 
                                    CreateProfessorSerializer,
                                    CreateDisciplinasSerializer,
                                    CreateBoletimSerializer)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CreateUserSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = CreateAlunoSerializer
    
class EgressoViewSet(viewsets.ModelViewSet):
    queryset = Egresso.objects.all()
    serializer_class = CreateEgressoSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais_aluno.objects.all()
    serializer_class = CreatePaisSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = CreateProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = CreateDisciplinasSerializer

class BoletimViewSet(viewsets.ModelViewSet):
    queryset = Boletim.objects.all()
    serializer_class = CreateBoletimSerializer

