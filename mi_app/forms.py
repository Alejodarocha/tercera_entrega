from django import forms
from .models import Libro
from django.contrib.auth.models import User


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'imagen', 'fecha_publicacion']




class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



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
