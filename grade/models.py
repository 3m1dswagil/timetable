# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Disciplina(models.Model):
    disciplina = models.CharField(max_length=50)
    cod_disc = models.CharField(max_length=50)

# Create your models here.
