from django.contrib.auth import login
from django.forms import ModelForm
from django import forms
from Primeflix.models import Episodio, Filme, Serie, Usuario

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
