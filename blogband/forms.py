from django import forms 
from .models import Artista

class CadastroArtista(forms.ModelForm):
    
    class Meta:
        model = Artista
        
        fields = [
            "nome",
            "estilo_musical",
            "pais",
            "descricao",
            "imagem"
        ]


        
      