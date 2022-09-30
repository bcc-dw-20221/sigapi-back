from enum import unique
from django.db import models
from django.contrib.auth import get_user_model

class Curso(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    matriz_curricular = models.CharField(max_length=9)
    data_vigor = models.DateField()
    
class Aluno(models.Model):
    """Dados do ALUNO"""
    choice = (
        ("C","casado"),
        ("S","solteiro"),
    )
    
    user = models.ForeignKey(get_user_model(),unique=True, on_delete=models.CASCADE,null=False,related_name="Aluno",)
    matricula = models.IntegerField(unique=True)
    endereco = models.CharField(max_length=120)
    born = models.DateField()
    cpf = models.IntegerField()
    nome_pai = models.CharField(max_length=120)
    nome_mae = models.CharField(max_length=120)
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=120, choices=choice)
    rg = models.CharField(max_length=10)

class Egresso(models.Model):
    """Dados do ALUNO"""
    choice = (
        ("C","casado"),
        ("S","solteiro"),
    )
    user = models.OneToOneField(
        
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        null=False,
        related_name="Egresso",
        )
    matricula = models.IntegerField(unique=True)
    endereco = models.CharField(max_length=120)
    born = models.DateField()
    cpf = models.IntegerField()
    nome_pai = models.CharField(max_length=120)
    nome_mae = models.CharField(max_length=120)
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=120, choices=choice)
    rg = models.CharField(max_length=10)

class Pais_aluno(models.Model):
    """Dados do pai do aluno"""
    user = models.OneToOneField(
        
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        null=False,
        related_name="pai de aluno +",
        )
    filho = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, related_name="filho")
    endereco = models.CharField(max_length=120)
    born = models.DateField()
    cpf = models.IntegerField()
    telefone = models.CharField(max_length=15)
    rg = models.CharField(max_length=9)

class Professor(models.Model):
    """Dados do PROFESSOR"""
    user = models.ForeignKey(get_user_model(),unique=True, on_delete=models.CASCADE,null=False,related_name="PROFESSOR",)
    cpf = models.IntegerField(unique=True)
    born = models.DateField(verbose_name=str)
    endereco = models.CharField(max_length=50)
    salario = models.FloatField()
    alvos = (
        ("B","Bacharelado"),
        ("L","Licenciatura"),
        ("T","Tecnólogo")
    )
    grau = models.CharField(max_length=15, choices=alvos)
    """titulação a decidir"""

class insituicao(models.Model):
    """instituição de formação do PROFESSOR"""
    nome = models.CharField(max_length=100)

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING, related_name="professor")
    qtd_horas = models.PositiveIntegerField()
    semestre = models.IntegerField()
    pre_requisito = models.CharField(max_length=90)

class Boletim(models.Model):
    estado = (
        ("C", "CURSANDO"),
        ("A", "APROVADO"),
        ("R", "REPROVADO")
    )
    aluno = models.OneToOneField(Aluno, on_delete=models.DO_NOTHING, null=False, related_name="aluno")
    status = models.CharField(max_length=9, choices=estado)
    disciplinas = models.ManyToManyField(Disciplina)

class Faltas(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, related_name="FaltasDele")
    data = models.DateField()
    isPresente = models.BooleanField(default=True)
    botelim = models.ForeignKey(Boletim, on_delete=models.DO_NOTHING, related_name="boletim")