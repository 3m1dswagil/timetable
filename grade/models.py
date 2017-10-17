# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Disciplina(models.Model):
    disciplina = models.CharField(max_length=50)
    cod_disc = models.CharField(max_length=50)

class Professor(models.Model):
    nome = models.CharField(max_length=70)
    cod_prof = models.CharField(max_length=12)
    disc_p = models.ManyToManyField(Disciplina)

class DiscMinistrada(models.Model):
    profId = models.ForeignKey(Professor, on_delete=models.CASCADE)
    discId = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

class Turma(models.Model):
    turma = models.CharField(max_length=50)
    cod_turma = models.CharField(max_length=50)

# Create your models hereself.
