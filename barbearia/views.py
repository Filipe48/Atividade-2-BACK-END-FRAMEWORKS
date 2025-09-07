from django.shortcuts import render, redirect

def pagina_login(request):

    if request.method == 'POST':
        return redirect('pagina_barbearia')

    return render(request, 'barbearia/login.html')

def pagina_barbearia(request):
    
    return render(request, 'barbearia/barbearia.html')
