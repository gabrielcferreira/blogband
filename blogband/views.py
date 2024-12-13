from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Artista
from .forms import CadastroArtista

def home(request):
    bandas = Artista.objects.all()
    return render(request, 'home.html', {'bandas': bandas})

   
def cadastro(request):
    
    if request.method == 'POST':
        form = CadastroArtista(request.POST, request.FILES)
        if form.is_valid():
            artista_cad = form.save(commit=False)
            artista_cad.user = request.user
            artista_cad.save()
            return redirect('busca')
    else:
        form = CadastroArtista()
        return render(request, 'cadastro.html', {'form': form})
        
            
  
  
  
  # RENOMEAR   
class ArtistaListView(ListView):
    model = Artista
    template_name = 'list-artistas.html'
    context_object_name = 'InfoArtista'
    
    def get_queryset(self):
        
       busca_artista = self.request.GET.get('país_artista')
       
       if busca_artista:
           artista_info = Artista.objects.filter(pais__icontains=busca_artista)
       else:
           artista_info = Artista.objects.all()     
        
             
       return artista_info
   
   
    
        
    
    
    
     
            
        
        
    

    