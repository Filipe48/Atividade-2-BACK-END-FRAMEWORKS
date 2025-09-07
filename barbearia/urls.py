from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_login, name='pagina_login'),
    path('barbearia/', views.pagina_barbearia, name='pagina_barbearia'),
]