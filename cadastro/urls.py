from django.urls import path
from . import views

urlpatterns = [
    path('', views.primeiraPagina, name='primeira_pagina'),
]