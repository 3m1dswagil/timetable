# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Disciplina(models.Model):
    disciplina = models.CharField(max_length=50)
    cod_disc = models.CharField(max_length=50)


class Professor(models.Model):
        Nome = models.CharField(max_length=50)
        disciplinas = models.ForeignKey('Disciplina')



class Aula(models.Model):
        NomeProf = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)


# Create your models her:
