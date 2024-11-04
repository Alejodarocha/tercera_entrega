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

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm
from django.contrib import messages


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado exitosamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/libro_form.html', {'form': form})


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
    return render(request, 'libros/libro_form.html', {'form': form})


def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, "Libro eliminado exitosamente.")
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})



from .models import Pagina
from .forms import PageForm

def update_page(request, pk):
    page = get_object_or_404(Pagina, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, "Página actualizada exitosamente.")
            return redirect('page_list')  # Asume que tienes una vista para listar páginas
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
    query = request.GET.get('q')
    resultados = None
    if query:
        resultados = Libro.objects.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
    if not resultados:
        mensaje = "No está ese libro aún"
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

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


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
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista para cerrar sesión (logout_view)
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
            return redirect('libro_list')  # Cambia esto según la URL a la que quieras redirigir
    else:
        form = PageForm()
    return render(request, 'crear_pagina.html', {'form': form})