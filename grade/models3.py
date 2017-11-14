# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


RESTRICAO_DIA_CHOICES = (
    ('0', 'Segunda'),
    ('1', 'Terça'),
    ('2', 'Quarta'),
    ('3', 'Quinta'),
    ('4', 'Sexta'),
)

RESTRICAO_HORA_CHOICES = (
    ('0', 'Primeira'),
    ('1', 'Segunda'),
    ('2', 'Terceira'),
    ('3', 'Quarta'),
    ('4', 'Quinta'),
    ('5', 'Sexta'),
)

TURNO_CHOICES = (
    ('0', 'Matutino'),
    ('1', 'Vespertino'),
    ('2', 'Noturno'),

)

class Escola(models.Model):
    nome = models.CharField(max_length=70)

class Coordenador(models.Model):
    nome = models.CharField(max_length=70)
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)
    escola = models.ForeignKey('Escola')

class Professor(models.Model):
    nome = models.CharField(max_length=70)
    codigo = models.CharField(max_length=12)
    #coordenador = models.ForeignKey('Coordenador')
    #disciplina = models.ForeignKey('Disciplina')
    restricao_dia_semana =  models.CharField(max_length=1, choices=RESTRICAO_DIA_CHOICES)
    restricao_horario =  models.CharField(max_length=1, choices=RESTRICAO_HORA_CHOICES)

    def __str__(self):
            return str(self.nome)

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
         return str(self.nome)

class Disciplina_ministrada(models.Model):
    codigo_disciplina = models.CharField(max_length=50)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)

class Turma(models.Model):
    nome = models.CharField(max_length=20)
    codigo = models.CharField(max_length=12)
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)
# Create your models here.
