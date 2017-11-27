# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Disciplina_form
from .forms import Professor_form
from .forms import Turma_form, Disciplina_ministrada_form
from django.views.generic import ListView
from grade.models import Disciplina, Professor, Turma, Disciplina_ministrada, Disciplina_turma
from django.template.response import TemplateResponse

# Create your views here.

def disciplina_new(request):
    form = Disciplina_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            disciplina = Disciplina()
            disciplina.codigo = form.cleaned_data['codigo']
            disciplina.nome = form.cleaned_data['nome']
            disciplina.carga_horaria = form.cleaned_data['carga_horaria']
            disciplina.save()
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
            turma = Turma()
            turma.nome = form.cleaned_data['nome']
            turma.codigo = form.cleaned_data['codigo']
            disciplina_ministrada = form.cleaned_data['disciplina_ministrada']
            turma.save()
            for codigo_disciplina in disciplina_ministrada:
                disciplina_habilitada = Disciplina_ministrada.objects.filter(pk=codigo_disciplina.pk)[0:1].get()

                disciplina_turma = Disciplina_turma()
                disciplina_turma.turma = turma
                disciplina_turma.disciplina_ministrada=disciplina_habilitada

                disciplina_turma.save()
            return redirect("turma_list")
    return render(request, 'grade/cad_turma.html', {'form': form})

# def disciplina_ministrada_new(request):
#     form = Disciplina_ministrada(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             disciplina_ministrada = form.cleaned_data['disciplina_ministrada']
#             disciplina_ministrada.save()


################################################################################
def disciplina_turma_list(request):
    dados2 = Disciplina_turma.objects.all()
    return TemplateResponse(request, 'grade/lista_turma.html', {'dados2': dados2})

def disciplina_list(request):
    data = Disciplina.objects.all()
    return TemplateResponse(request, 'grade/lista_disc.html', {'data': data})

def professor_list(request):
    datas = Disciplina_ministrada.objects.all()
    return TemplateResponse(request, 'grade/lista_prof.html', {'datas': datas})

def turma_list(request):
    data2 = Disciplina_turma.objects.all()
    return TemplateResponse(request, 'grade/lista_turma.html', {'data2': data2})

def pagina_inicial(request):
    return render(request, 'grade/pag_inicial.html')
