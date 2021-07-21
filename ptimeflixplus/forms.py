from django.forms import ModelForm
from django import forms
from Primeflix.models import Episodio, Filme, Serie

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