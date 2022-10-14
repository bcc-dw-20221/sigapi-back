from multiprocessing.connection import wait
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from SIGAPI_rest.models import Curso, Aluno, Egresso, Pais_aluno, Professor, Disciplina, Boletim
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from SIGAPI_rest.serializer import (CursoSerializer, 
                                    CreateUserSerializer, 
                                    CreateAlunoSerializer, 
                                    CreateEgressoSerializer, 
                                    CreatePaisSerializer, 
                                    CreateProfessorSerializer,
                                    CreateDisciplinasSerializer,
                                    CreateBoletimSerializer)

class CursoViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class UserViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['=username', '=email']
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = CreateUserSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['=matricula', 'cpf', 'user__username']
    permission_classes = [IsAuthenticated]
    queryset = Aluno.objects.all()
    serializer_class = CreateAlunoSerializer
    
class EgressoViewSet(viewsets.ModelViewSet):
    queryset = Egresso.objects.all()
    serializer_class = CreateEgressoSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais_aluno.objects.all()
    serializer_class = CreatePaisSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['=cpf', '=user__username']
    permission_classes = [IsAuthenticated]
    queryset = Professor.objects.all()
    serializer_class = CreateProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['=nome','=semestre' , '=user__username']
    permission_classes = [IsAuthenticated]
    queryset = Disciplina.objects.all()
    serializer_class = CreateDisciplinasSerializer

class BoletimViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['=aluno__matricula']
    permission_classes = [IsAuthenticated]
    queryset = Boletim.objects.all()
    serializer_class = CreateBoletimSerializer

