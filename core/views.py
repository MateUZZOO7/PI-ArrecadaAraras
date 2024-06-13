from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CadastroForm, DoacaoForm, LoginForm
from .services import CadastroClienteService

def index(request):
    return render(request, "index.html")

def cadastro_view(request):
    if request.method == "POST":
        form_cadastro = CadastroForm(request.POST)
        if form_cadastro.is_valid():
            try:
                form_cadastro.registrar_cliente(request)
                return redirect("core:index")
            except ValidationError as e:
                form_cadastro.add_error(None, e.message)
    else:
        form_cadastro = CadastroForm()
    
    contexto = {"form_cadastro": form_cadastro}
    return render(request, "cadastro.html", contexto)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login bem-sucedido.")
                return redirect(reverse('core:index'))
            else:
                return render(request, "login.html", {"form": form, "error_message": "Credenciais inválidas."})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('core:index')

def ongs_view(request):
    return render(request, "ongs.html")

@login_required
def doacao_view(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = DoacaoForm()
    return render(request, 'ongs.html', {'form': form})
