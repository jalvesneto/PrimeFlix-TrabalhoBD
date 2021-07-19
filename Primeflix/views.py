from django.http import request, HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, "index.html")

def telaCadastrar(request):
    return render(request, "telacadastro.html")

def main(request):
    return render(request, "main.html")