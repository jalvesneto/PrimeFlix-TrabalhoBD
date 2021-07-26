from Primeflix.models import Serie, Titulo, Filme, Episodio, Usuario
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from ptimeflixplus.forms import EpisodioForm, FilmeForm, SerieForm, UsuarioForm
from django.core.paginator import Paginator

def loginUsuario(request):
    if request.method == 'POST':
        email = request.POST['usuario']
        senha = request.POST['senha']
        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect(main)
        else:
            messages.error(request, "email ou senha errado!!")
    return render(request, 'index.html')
    
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
    data['pk'] = pk
    if request.method == 'POST':
        FormEpisodio = EpisodioForm(request.POST)
        print(request.POST)
        FormEpisodio.save()
        return redirect('series')
    else:
        data['form'] = EpisodioForm()
    return render(request, "addep.html", data)

def verTtulos(request):
    data = {}
    alltitulos = Titulo.objects.all()
    paginator = Paginator(alltitulos, 5)
    pages=request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'vcatalogo.html', data)

def viewTitulo(request, pk):
    data = {}
    data['dbtitulo'] = Titulo.objects.get(idtitulo=pk)
    if Serie.objects.filter(titulo_ptr_id=pk).exists():
        data['dbserie'] = Serie.objects.get(titulo_ptr_id=pk)
        allep = Episodio.objects.filter(fk_serie=pk).order_by('temporada', 'numero')
        paginator = Paginator(allep, 3)
        pages=request.GET.get('page')
        data['dbepisode'] = paginator.get_page(pages)
        return render(request, 'viewTituloSerie.html', data)
    else:
        data['dbfilme'] = Filme.objects.get(titulo_ptr_id=pk)
        return render(request, 'viewTituloFilme.html', data)
    

def update(request,pk):
    titulo = {}
    titulo['db'] = Titulo.objects.get(idtitulo=pk)
    if Serie.objects.filter(titulo_ptr_id=pk).exists():
        titulo['db2'] = Serie.objects.get(titulo_ptr_id=pk)
        if request.method == "POST":          
            form = SerieForm(request.POST or None, instance=titulo['db2'])
            if form.is_valid:
                form.save()
                return redirect('verTitulos')
        else:
            titulo['dbs'] = SerieForm(instance = titulo['db'])
        return render(request, 'adserie.html', titulo)
    else:
        titulo['db2'] = Filme.objects.get(titulo_ptr_id=pk)
        if request.method == "POST":
            form = FilmeForm(request.POST or None, instance=titulo['db2'])
            if form.is_valid:
                form.save()
                return redirect('verTitulos')
        else:  
            titulo['dbs'] = FilmeForm(instance=titulo['db'])
        return render(request, 'adfilme.html', titulo)   
    
def updateEp(request,pk,fk):
    data = {}
    data['ep'] = Episodio.objects.get(id_ep=pk)
    data['fk'] = fk
    if request.method == 'POST':
        FormEpisodio = EpisodioForm(request.POST or None, instance=data['ep'])
        print(request.POST)
        FormEpisodio.save()
        return redirect('series')
    return render(request, "addep.html", data)

def delete(request, pk):
    titulo = Titulo.objects.get(idtitulo=pk)
    titulo.delete()
    return redirect('verTitulos')

def deleteep(request,pk, fk):
    ep = Episodio.objects.get(id_ep=pk)
    ep.delete()
    return redirect(request.META['HTTP_REFERER'])

def cria_user_django(info):
    user = User.objects.create_user(info['email'], info['email'], info['senha'])
    user.save()

def cadUsuario(request):
    data = {}
    if request.method == "POST":
        user = UsuarioForm(request.POST)
        if user.is_valid():
            cria_user_django(request.POST)
            user.save()
            return redirect("/")
    else:
        user = UsuarioForm()
    data['form'] = user
    return render(request, "telaCadastro.html", data)

