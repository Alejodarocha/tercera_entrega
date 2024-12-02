from django import forms
from .models import Libro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'imagen', 'fecha_publicacion']





class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()  
        return user
    

class ProfileForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=500, required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'descripcion', 'imagen']



from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo', 'autor', 'descripcion', 'fecha', 'imagen']
