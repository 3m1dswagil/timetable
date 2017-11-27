# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Disciplina
from .models import Disciplina_ministrada, Disciplina_turma
from .models import Professor
from .models import Turma
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

CARGA_HORARIA_CHOICES = (
    ('0', '1 aula'),
    ('1', '2 aulas'),
    ('2', '3 aulas'),
    ('3', '4 aulas'),
    ('4', '5 aulas'),
    ('5', '6 aulas'),
)

'''class Disciplina_form(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ['codigo', 'nome', 'carga_horaria']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '123matematica123'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': 'Matematica'}),
            'carga_horaria': forms.ChoiceField(choices=CARGA_HORARIA_CHOICES, widget=forms.RadioSelect())
        }

        error_messages = {
            'nome':{
                'required': 'Este campo é obrigatório'
            },
            'codigo':{
                'required': 'Este campo é obrigatório'
            },
        }
'''
class Disciplina_form(forms.Form):
    codigo = forms.CharField(label='Código', max_length=20)
    nome = forms.CharField(label='Nome', max_length=100)
    carga_horaria = forms.ChoiceField(choices=CARGA_HORARIA_CHOICES, widget=forms.RadioSelect())


RESTRICAO_DIA_CHOICES = (
    ('0', 'Nenhuma'),
    ('2', 'Segunda'),
    ('3', 'Terça'),
    ('4', 'Quarta'),
    ('5', 'Quinta'),
    ('6', 'Sexta'),
)

RESTRICAO_HORA_CHOICES = (
    ('0', 'Nenhuma'),
    ('1', 'Primeira'),
    ('2', 'Segunda'),
    ('3', 'Terceira'),
    ('4', 'Quarta'),
    ('5', 'Quinta'),
    ('6', 'Sexta'),
    ('7', 'Todas'),

)
class Professor_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    codigo = forms.CharField(label='Matrícula', max_length=100)
    disciplinas = forms.ModelMultipleChoiceField(queryset=Disciplina.objects.all())
    restricao_dia_semana = forms.ChoiceField(choices=RESTRICAO_DIA_CHOICES, widget=forms.RadioSelect())
    restricao_horario = forms.MultipleChoiceField(choices=RESTRICAO_HORA_CHOICES, widget=forms.CheckboxSelectMultiple())

class Disciplina_ministrada_form(forms.Form):
    codigo_disciplina = forms.CharField(label='Codigo', max_length=15)
    professor_disciplina = forms.ModelMultipleChoiceField(queryset=Disciplina_ministrada.objects.all())

class Turma_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    codigo = forms.CharField(label='Código', max_length=100)
    disciplina_ministrada = forms.ModelMultipleChoiceField(queryset=Disciplina_ministrada.objects.all())

class Disciplina_turma(forms.Form):
    turma = forms.ModelMultipleChoiceField(queryset=Disciplina_ministrada.objects.all())
    disciplina_ministrada = forms.ModelMultipleChoiceField(queryset=Disciplina_ministrada.objects.all())
