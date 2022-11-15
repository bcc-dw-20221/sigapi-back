from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    matriz_curricular = models.CharField(max_length=9)
    data_vigor = models.DateField()
     