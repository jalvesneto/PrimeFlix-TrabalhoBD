from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from ptimeflixplus.forms import FilmeForm

def home(request):
    return render(request, "index.html")

def telaCadastrar(request):
    return render(request, "telacadastro.html")

def main(request):
    return render(request, "main.html")

def addFilme(request):
    data = {}
    if request.method == 'POST':
        formFilme = FilmeForm(request.POST)
        # print(request.POST['nome'],request.POST['sinopse'],request.POST['ano'],request.POST['datalancamento'])
        # formFilme.titulo = request.POST['nome']
        # formFilme.sinopse = request.POST['sinopse']
        # formFilme.ano = request.POST['ano']
        # print(formFilme.ano)
        # formFilme.datalancamento = request.POST['datalancamento']
        formFilme.save()
        return render(request, 'main')
    else:
        formFilme = FilmeForm()
    data['form'] = formFilme
    return render(request, "adfilme.html", data)