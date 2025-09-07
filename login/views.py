from django.shortcuts import render

def pagina_externa(request):
    return render (request, 'login/pagina.html')
