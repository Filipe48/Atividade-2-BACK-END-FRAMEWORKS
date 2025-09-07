from django.shortcuts import render
from django.http import HttpResponse

def primeiraPagina(request):
    return HttpResponse("Seu nome e sua matrícula")
