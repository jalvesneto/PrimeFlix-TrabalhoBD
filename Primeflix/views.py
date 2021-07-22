from Primeflix.models import Serie, Titulo, Filme
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from ptimeflixplus.forms import EpisodioForm, FilmeForm, SerieForm

def home(request):
    return render(request, "index.html")

def sair(request):
    return render(request, "index.html")

def telaCadastrar(request):
    return render(request, "telacadastro.html")

def main(request):
    return render(request, "main.html")

def addFilme(request):
    data = {}
    if request.method == 'POST':
        formFilme = FilmeForm(request.POST)
        formFilme.save()
        return redirect('main')
        
    else:
        formFilme = FilmeForm()
    data['form'] = formFilme
    return render(request, "adfilme.html", data)

def addSerie(request):
    data = {}
    if request.method == 'POST':
        formSerie = SerieForm(request.POST)
        formSerie.save()
        return redirect('main')
    else:
        formSerie = SerieForm()
    data['form'] = formSerie
    return render(request, "adserie.html", data)

def series(request):
    data, series = {}, {}
    series['serie'] = Serie.objects.all()
    data['titulo'] = Titulo.objects.filter(idtitulo__in=series['serie'].values_list('titulo_ptr_id'))
    return render(request, "viewSeries.html", data)

def addEp(request,pk):
    data = {}
    data['db'] = Serie.objects.get(titulo_ptr_id=pk)
    if request.method == 'POST':
        FormEpisodio = EpisodioForm(request.POST, instance=data['db'])
        FormEpisodio.save()
        return redirect('series')
    else:
        data['form'] = EpisodioForm(instance=data['db'])
    return render(request, "addep.html", data)

def verTtulos(request):
    data = {}
    data['db'] = Titulo.objects.all()
    return render(request, 'vcatalogo.html', data)

def viewTitulo(request, pk):
    data = {}
    data['dbtitulo'] = Titulo.objects.get(idtitulo=pk)
    if Serie.objects.filter(titulo_ptr_id=pk).exists():
        data['dbserie'] = Serie.objects.get(titulo_ptr_id=pk)
        return render(request, 'viewTituloSerie.html', data)
    else:
        data['dbfilme'] = Filme.objects.get(titulo_ptr_id=pk)
        return render(request, 'viewTituloFilme.html', data)
    

def update(request,pk):
    titulo = {}
    titulo['db'] = Titulo.objects.get(idtitulo=pk)
    if Serie.objects.filter(titulo_ptr_id=pk).exists():
        if request.method == "POST":
            form = SerieForm(request.POST or None, instance=titulo['db'])
            if form.is_valid:
                form.save()
                return redirect('verTitulos')
        else:
            titulo['db2'] = Serie.objects.get(titulo_ptr_id=pk)
            titulo['dbs'] = SerieForm(instance=titulo['db'])
        return render(request, 'adSerie.html', titulo)
    else:
        if request.method == "POST":
            form = FilmeForm(request.POST or None, instance=titulo['db'])
            if form.is_valid:
                form.save()
                return redirect('verTitulos')
        else:
            titulo['db2'] = Filme.objects.get(titulo_ptr_id=pk)
            titulo['dbs'] = FilmeForm(instance=titulo['db'])
        return render(request, 'adFilme.html', titulo)   
    

def delete(request, pk):
    titulo = Titulo.objects.get(idtitulo=pk)
    titulo.delete()
    return redirect('verTitulos')