from django.db import models
from django.contrib.auth.models import User



class Artista(models.Model):
    nome = models.CharField(max_length=30)
    estilo_musical = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artistas')
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        
        return self.nome
        

        
        