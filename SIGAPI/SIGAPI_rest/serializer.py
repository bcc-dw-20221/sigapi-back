from operator import ge
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response
from SIGAPI_rest.models import Curso, Aluno, Egresso, Pais_aluno, Professor,Disciplina, Faltas, Boletim

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Curso
        fields = "_all_"

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = [
            "url",
            "nome",
            "matriz_curricular",
            "data_vigor"
        ]

        def create(self, validated_data):
            curso, created = Curso.objects.update_or_create(
                nome = validated_data.pop("nome"),
                matriz_curricular = validated_data.pop("matriz_curricular"),
                data_vigor = validated_data.pop("data_vigor"),
            )
            if created:
                return curso
            else:
                return Response(
                    {"message": "Não pude criar o curso"}, status=406
                )
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = get_user_model()
        fields = ["url","username"]

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "password"},
    )
    class Meta:
        model = get_user_model()
        fields = [
            "url",
            "username",
            "password",
            "email",
        ]
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(CreateUserSerializer, self).create(validated_data)

class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ["url", "username"]

class CreateAlunoSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer

    class Meta:
        model = Aluno
        fields = [
            "url",
            "user",
            "matricula",
            "cpf",
            "born",
            "endereco",
            "nome_pai",
            "nome_mae",
            "sexo",
            "telefone",
            "estado_civil",
            "rg",
        ]
        def create(self, validated_data):
            user = get_user_model().objects.filter(url=validated_data.get("user"))
            if user.pk:
                aluno,created = Aluno.objects.update_or_create(
                    user = user,
                    matricula = validated_data.pop("matricula"),
                    cpf = validated_data.pop("cpf"),
                    born = validated_data.pop("born"),
                    endereco = validated_data.pop("endereco"),
                    nome_pai = validated_data.pop("nome_pai"),
                    nome_mae = validated_data.pop("nome_mae"),
                    sexo = validated_data.pop("sexo"),
                    telefone = validated_data.pop("telefone"),
                    estado_civil = validated_data.pop("estado_civil"),
                    rg = validated_data.pop("rg"),

                )
                if created:
                    return aluno
            else:
                user.delete()
            return Response(
                {"message": "Não pude criar um novo aluno"}, status=406
            )
            
class CreateEgressoSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer

    class Meta:
        model = Egresso
        fields = ["url", "user", "matricula", "cpf", "born","endereco",
            "nome_pai", "nome_mae", "sexo", "telefone", "estado_civil", "rg",
        ]

        def create(self, validated_data):
        
            user = get_user_model().objects.filter(url=validated_data.get("user"))
            if user.pk:
                egresso,created = Egresso.objects.update_or_create(
                    user = user,
                    matricula = validated_data.pop("matricula"),
                    cpf = validated_data.pop("cpf"),
                    born = validated_data.pop("born"),
                    endereco = validated_data.pop("endereco"),
                    nome_pai = validated_data.pop("nome_pai"),
                    nome_mae = validated_data.pop("nome_mae"),
                    sexo = validated_data.pop("sexo"),
                    telefone = validated_data.pop("telefone"),
                    estado_civil = validated_data.pop("estado_civil"),
                    rg = validated_data.pop("rg"),

                )
                if created:
                    return egresso
            else:
                user.delete()
            return Response(
                {"message": "Não pude criar um novo aluno"}, status=406
            )
                  
class CreatePaisSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer

    class Meta:
        model = Pais_aluno
        fields = [
            "url",
            "user",
            "filho",
            "endereco",
            "born",
            "cpf",
            "telefone",
            "rg",
        ]
        def create(self, validated_data):
        
            user_data = validated_data.pop("user")

            user = UserSerializer.create(
                UserSerializer(), validated_data=user_data)
            if user.pk:
                pais,created = Aluno.objects.update_or_create(
                    user = user,
                    filho = Aluno.objects.filter(pk=validated_data.get("filho")),
                    cpf = validated_data.pop("cpf"),
                    born = validated_data.pop("born"),
                    endereco = validated_data.pop("endereco"),
                    telefone = validated_data.pop("telefone"),
                    rg = validated_data.pop("rg"),

                )
                if created:
                    return pais
            else:
                user.delete()
            return Response(
                {"message": "Não pude criar um novo pai"}, status=406
            )

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Professor
        fields = ["url", "username", "id"]

class CreateProfessorSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer
    class Meta:
        model = Professor
        fields = [
            "url",
            "user",
            "cpf",
            "born",
            "endereco",
            "salario",
            "grau",
        ]
        def create(self, validated_data):
            user = get_user_model().objects.filter(url=validated_data.get("user"))

            if user.pk:
                professor,created = Professor.objects.update_or_create(
                    user = Professor.objects.filter(pk=user.pk),
                    cpf = validated_data.pop("cpf"),
                    born = validated_data.pop("born"),
                    endereco = validated_data.pop("endereco"),
                    salario = validated_data.pop("salario"),
                    grau = validated_data.pop("grau"),
                )
                if created:
                    return professor
            else:
                user.delete()
            return Response({"message": "Não pude criar um novo professor"}, status=406)

class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Disciplina
        fields = ["url","nome"]

class CreateDisciplinasSerializer(serializers.HyperlinkedModelSerializer):
    prof = CreateProfessorSerializer

    class Meta:
        model = Disciplina
        fields = [
            "url",
            "nome",
            "professor",
            "qtd_horas",
            "semestre",
            "pre_requisito",
        ]
        def create(self, validated_data):
            prof = Professor.objects.filter(url=validated_data.get("user"))
            disciplina ,created = Disciplina.objects.update_or_create(
                professor = prof,
                nome = validated_data.pop("nome"),
                qtd_horas = validated_data.pop("qtd_horas"),
                semestre = validated_data.pop("semestre"),
                pre_requisito = validated_data.pop("pre_requisito"),
            )
            if created:
                return disciplina
            return Response({"message": "Não pude criar um novo professor"}, status=406)

class CreateBoletimSerializer(serializers.HyperlinkedModelSerializer):
    aluno = CreateAlunoSerializer
    disciplinas = CreateDisciplinasSerializer(many=True)

    class Meta:
        model = Boletim
        fields = [
            "aluno",
            "disciplinas",
            "status"
        ]
    def create(self, validated_data):
        
            id = validated_data.pop("aluno")
            id2 = validated_data.pop("disciplinas")
            
            disciplinas = DisciplinaSerializer.create(DisciplinaSerializer(), validated_data=id2)
            aluno = AlunoSerializer.create(AlunoSerializer(), validated_data=id)
            boletim ,created = Disciplina.objects.update_or_create(
                status = validated_data.pop("status"),
                aluno = aluno,
                disciplinas = disciplinas,
            )
            if created:
                return boletim
            return Response({"message": "Não pude criar um novo professor"}, status=406)

class CreateFaltasSerializer(serializers.HyperlinkedModelSerializer):
    aluno = AlunoSerializer
    

    class Meta:
        model = Faltas
        fields = [
            "aluno",
            "data",
            "isPresent",
            "boletim"
        ]


