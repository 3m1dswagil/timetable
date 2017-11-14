# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Disciplina_form
from .forms import Professor_form
from .forms import Turma_form
from django.views.generic import ListView
from grade.models import Disciplina, Professor, Turma, Disciplina_ministrada
from django.template.response import TemplateResponse

# Create your views here.

def disciplina_new(request):
    form = Disciplina_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("disciplina_list")
    return render(request, 'grade/cad_disc.html', {'form': form})

def professor_new(request):
    form = Professor_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            professor = Professor()
            professor.nome = form.cleaned_data['nome']
            professor.codigo = form.cleaned_data['codigo']
            disciplinas = form.cleaned_data['disciplinas']
            professor.restricao_horario = form.cleaned_data['restricao_horario']
            professor.restricao_dia_semana = form.cleaned_data['restricao_dia_semana']
            professor.save()
            for nome in disciplinas:

                disciplina_habilitada = Disciplina.objects.filter(nome=nome)[0:1].get()

                disciplina_ministrada = Disciplina_ministrada()
                disciplina_ministrada.professor = professor
                disciplina_ministrada.codigo = professor.codigo + disciplina_habilitada.codigo
                disciplina_ministrada.disciplina = disciplina_habilitada
                disciplina_ministrada.save()

            return redirect("professor_list")

    return render(request, 'grade/cad_prof.html', {'form': form})

def turma_new(request):
    form = Turma_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("turma_list")
    return render(request, 'grade/cad_turma.html', {'form': form})

################################################################################
def disciplina_list(request):
    data = Disciplina.objects.all()
    return TemplateResponse(request, 'grade/lista_disc.html', {'data': data})

def professor_list(request):
    datas = Disciplina_ministrada.objects.all()
    return TemplateResponse(request, 'grade/lista_prof.html', {'datas': datas})

def turma_list(request):
    data2 = Turma.objects.all()
    return TemplateResponse(request, 'grade/lista_turma.html', {'data2': data2})

def pagina_inicial(request):
    return render(request, 'grade/pag_inicial.html')
