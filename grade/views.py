# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import DiscForm
from .forms import ProfForm
from django.views.generic import ListView
from grade.models import Disciplina
from grade.models import Professor
from django.template.response import TemplateResponse

# Create your views here.

def disc_new(request):
    form = DiscForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'grade/cad_disc.html', {'form': form})

def prof_new(request):
    form = ProfForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'grade/cad_prof.html', {'form': form})

def disc_list(request):
    data = Disciplina.objects.all()
    return TemplateResponse(request, 'grade/lista_disc.html', {'data': data})

def prof_list(request):
    data = Professor.objects.all()
    return TemplateResponse(request, 'grade/lista_prof.html', {'data': data})


def pag_incial(request):
    return render(request, 'grade/pag_inicial.html')
