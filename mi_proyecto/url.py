from django.contrib import admin
from django.urls import path
from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.insertar_libro, name='insertar_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]