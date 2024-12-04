from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm


from django.contrib.auth import login

from django.contrib import messages
from .models import Profile





def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, "¡Te has registrado correctamente!")
            return redirect('home') 
        else:
            messages.error(request, "Error al registrarse.")
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import ProfileForm

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Profile





@login_required
def profile(request):
    profile = request.user.profile  
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  
            messages.success(request, "Perfil actualizado exitosamente.")
            return redirect('profile')  
    else:
        form = ProfileForm(instance=profile)  

    return render(request, 'profile.html', {'form': form, 'profile': profile})

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()  
            update_session_auth_hash(request, form.user)  
            messages.success(request, '¡Contraseña cambiada exitosamente!')
            return redirect('profile')  
        else:
            messages.error(request, 'Por favor, corrija los errores.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm
from django.contrib import messages


from django.views.generic.list import ListView

class ListaLibroView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'lista_libro.html'  
    context_object_name = 'libros'  



from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Libro

class CrearLibroView(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ['titulo', 'autor', 'descripcion', 'fecha_publicacion']
    template_name = 'crear_libro.html'  
    success_url = reverse_lazy('lista_libro') 



from django.views.generic.edit import UpdateView

class ActualizarLibroView(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ['titulo', 'autor', 'descripcion', 'fecha_publicacion']
    template_name = 'libro_form.html'  
    success_url = reverse_lazy('lista_libro') 



from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden

from django.views.generic.edit import DeleteView

class EliminarLibroView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'libro_delete.html'  
    success_url = reverse_lazy('lista_libro')  



from .models import Page
from .forms import PageForm

def update_page(request, pk):
    page = get_object_or_404(Pagina, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, "Página actualizada exitosamente.")
            return redirect('page_list')  
    else:
        form = PageForm(instance=page)
    return render(request, 'pages/page_form.html', {'form': form})

def delete_page(request, pk):
    page = get_object_or_404(Pagina, pk=pk)
    if request.method == 'POST':
        page.delete()
        messages.success(request, "Página eliminada exitosamente.")
        return redirect('page_list')
    return render(request, 'pages/page_confirm_delete.html', {'page': page})




from django.db.models import Q
from .models import Libro

def buscar_libro(request):
    query = request.GET.get('q', '')
    resultados = []
    mensaje = ""  

    if query:
        resultados = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(autor__icontains=query)
        if not resultados:  
            mensaje = "No se encontraron libros."

    return render(request, 'buscar_libro.html', {'resultados': resultados, 'query': query, 'mensaje': mensaje})


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido, {user.username}!")
                return redirect('home') 
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Por favor, corrige los errores del formulario.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages  

def logout_view(request):
    logout(request)  
    messages.success(request, "Has cerrado sesión exitosamente.")  
    return redirect('home')

from .forms import PageForm
from django.contrib import messages

def crear_pagina(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Página creada exitosamente.")
            return redirect('lista_libro') 
    else:
        form = PageForm()
    return render(request, 'crear_pagina.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Page  
def page_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  
    return render(request, 'page_detail.html', {'libro': libro})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import PageForm  

def page_edit(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  
    
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)  
        if form.is_valid():
            form.save()  
            return redirect('page_detail', pk=libro.pk)  
    else:
        form = LibroForm(instance=libro)  

    return render(request, 'page_edit.html', {'form': form, 'libro': libro})