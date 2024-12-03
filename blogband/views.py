from django.shortcuts import render
from .models import Artista

def home(request):
    bandas = Artista.objects.all()
    
    return render(request, 'index.html', {'bandas': bandas})