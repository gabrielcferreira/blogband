from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulário personalizado
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obrigatório. Informe um e-mail válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# Views
def logout_view(request):
    """Faz o logout do usuário"""
    logout(request)
    return redirect('home')  # Redireciona para a página inicial

def register(request):
    """Cadastra um novo usuário"""
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        # Processa o formulário do usuário
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(
                username=new_user.username,
                password=request.POST['password1']
            )
            login(request, authenticate_user)  # Loga o usuário automaticamente
            return redirect('home')  # Redireciona para a página inicial

    context = {'form': form}
    return render(request, 'users/register.html', context)
