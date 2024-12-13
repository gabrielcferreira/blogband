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
        
        def clean(self):
            nome = self.cleanead_data.get('nome')
            estilo_musical = self.cleanead_data.get('estio_musical')
            pais = self.cleanead_data.get('pais')
            descricao = self.cleanead_data.get('descricao')
            imagem = self.cleanead_data.get('imagem')


        
      