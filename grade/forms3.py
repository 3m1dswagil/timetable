# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Disciplina
from .models import Professor
from .models import Turma
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

'''
class Professor_form(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ['nome', 'codigo', 'restricao_dia_semana', 'restricao_horario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome do professor'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': '123prof123'}),
            'restricao_dia_semana': forms.RadioSelect(),
            'restricao_horario': forms.RadioSelect()

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
class Professor_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    codigo = forms.CharField(label='Matrícula', max_length=100)
    disciplinas = forms.ModelMultipleChoiceField(queryset=Disciplina.objects.all())
    restricao_dia_semana = forms.ChoiceField(choices=RESTRICAO_DIA_CHOICES, widget=forms.RadioSelect())
    restricao_horario = forms.MultipleChoiceField(choices=RESTRICAO_HORA_CHOICES, widget=forms.CheckboxSelectMultiple())


class Turma_form(forms.ModelForm):

    class Meta:
        model = Turma
        fields = ['codigo', 'nome']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '3m1'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '3m1'}),
        }

        error_messages = {
            'nome':{
                'required': 'Este campo é obrigatório'
            },
            'codigo':{
                'required': 'Este campo é obrigatório'
            },
        }
