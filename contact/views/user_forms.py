from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm
from django.contrib import auth

def register(request):
    form = RegisterForm()
    
    # messages.info(request, 'Um texto qualquer!')
    # messages.success(request, 'Um texto qualquer!')
    # messages.warning(request, 'Um texto qualquer!')
    # messages.error(request, 'Um texto qualquer!')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado')
            return redirect('contact:login')
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )


def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Logado com sucesso!')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'Login inválido!')
    
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )
    
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')