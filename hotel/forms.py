from django import forms
from .models import Quarto

class FormNome(forms.Form):
    nome = forms.CharField(label="Seu nome", max_length=40)
    email = forms.EmailField(label="Seu e-mail")
    idade = forms.IntegerField(label="Sua idade")
    data = forms.DateField(label="Data de nascimento", widget=forms.DateInput(attrs={'type': 'date'}))
    quartos = forms.CharField(label="Quantidade de quartos")
    # Campo de seleção dropdown
    quartos = forms.ModelChoiceField(queryset=Quarto.objects.all())
    

    # CHOICES = (
    #     ('', 'Opção 1'),
    #     ('opção2', 'Opção 2'),
    #     ('opção3', 'Opção 3'),
    # )