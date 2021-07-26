from django.contrib.auth import login
from django.forms import ModelForm
from django import forms
from Primeflix.models import Episodio, Filme, Genero, Possui, Serie, Usuario

class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'

class EpisodioForm(ModelForm):
    class Meta:
        model = Episodio
        fields = '__all__'


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class PossuiForm(ModelForm):
    class Meta:
        model = Possui
        fields = '__all__'

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
