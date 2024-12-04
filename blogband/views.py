from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Artista
from .forms import CadastroArtista

def home(request):
    bandas = Artista.objects.all()
    return render(request, 'home.html', {'bandas': bandas})

def logar(request):
    if request.user.is_authenticated:
        return redirect('cadastro')
    else:
        return redirect ('login')
    
def cadastro(request):
    form= CadastroArtista()
    return render(request, 'cadastro.html', {'form': form})
    
  
    

    