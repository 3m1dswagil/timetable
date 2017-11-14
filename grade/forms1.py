# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Disciplina, Disciplina_ministrada
from .models import Professor
from .models import Turma
# from .models import Relacao_disciplina_ch
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple


class Disciplina_form(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ['codigo', 'nome']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '123matematica123'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': 'Matematica'}),
        }

        error_messages = {
            'nome':{
                'required': 'Este campo é obrigatório'
            },
            'codigo':{
                'required': 'Este campo é obrigatório'
            },
        }

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

CARGA_HORARIA_CHOICES = (
    ('0', '1 AULA'),
    ('1', '2 AULAS'),
    ('2', '3 AULAS'),
    ('3', '4 AULAS'),

)

class Professor_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    codigo = forms.CharField(label='Matrícula', max_length=100)
    disciplinas = forms.ModelMultipleChoiceField(queryset=Disciplina.objects.all())
    restricao_dia_semana = forms.ChoiceField(choices=RESTRICAO_DIA_CHOICES, widget=forms.RadioSelect())
    restricao_horario = forms.MultipleChoiceField(choices=RESTRICAO_HORA_CHOICES, widget=forms.CheckboxSelectMultiple())

class Disciplina_ministrada_form(forms.ModelForm):

    class Meta:
        model = Disciplina_ministrada
        fields = ['professor', 'disciplina']
        widgets = {
            'professor': forms.ModelMultipleChoiceField(queryset=Professor.objects.all()),
            'disciplina': forms.ModelMultipleChoiceField(queryset=Disciplina.objects.all()),
        }


class Turma_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    codigo = forms.CharField(label='Código', max_length=100)
    disciplina_disponivel = forms.MultipleChoiceField(queryset=Disciplina_ministrada.objects.all())
    carga_horaria = forms.ChoiceField(choices=CARGA_HORARIA_CHOICES, widget=forms.RadioSelect())


'''class Turma_form(forms.ModelForm):

    class Meta:
        model = Turma
        fields = ['codigo', 'nome', 'disciplina', 'carga_horaria']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '3m1'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '3m1'}),
            'disciplina_carga_horaria': forms.ChoiceField(choices='Relacao_disciplina_ch'),

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
