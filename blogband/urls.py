from django.urls import path
from . import views
from .views import ArtistaListView

urlpatterns = [
    path("", views.home, name="home"),    
    path("cadastro/", views.cadastro, name="cadastro"),
    path("busca/", ArtistaListView.as_view(), name="busca"),
    
    
    
] 