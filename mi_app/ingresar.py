from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import LibroForm
from .models import Libro

# Vista para insertar libros
def insertar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirige a la vista principal
    else:
        form = LibroForm()
    return render(request, 'mi_app/insertar_libro.html', {'form': form})

# Vista para buscar libros
def buscar_libro(request):
    query = request.GET.get('q')  # Obtener la consulta del usuario
    resultados = None
    if query:
        resultados = Libro.objects.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
    return render(request, 'mi_app/buscar_libro.html', {'resultados': resultados})