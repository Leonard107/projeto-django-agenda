from django.db import models
from contatos.models import Contato
from django import forms
from django.forms import ModelForm

class FormContato(ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'descricao', 'categoria', 'mostrar', 'foto']

