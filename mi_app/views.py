from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ProfileForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm
from django.contrib import messages


def lista_libro(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libro.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro agregado de manera exitosa.") 
            return redirect('lista_libro')  
    else:
        form = LibroForm()
    return render(request, 'libro_form.html', {'form': form})


def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado exitosamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro_form.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden

def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  

    if request.method == "POST":
        libro.delete()  
        return redirect('lista_libro')  
    else:
        return HttpResponseForbidden()


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
               
                if not hasattr(user, 'profile'):
                    Profile.objects.create(user=user)  
                messages.success(request, f"Bienvenido, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

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

