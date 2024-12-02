from django.urls import path
from .views import (
    home, about, signup, profile, login_view, logout_view, buscar_libro,
    CrearLibroView, ListaLibroView, ActualizarLibroView, EliminarLibroView
)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('buscar/', buscar_libro, name='buscar_libro'),
  
    #  CRUD CON CBV
    path('libros/', ListaLibroView.as_view(), name='lista_libro'),
    path('libros/crear/', CrearLibroView.as_view(), name='crear_libro'),
    path('libros/<int:pk>/editar/', ActualizarLibroView.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', EliminarLibroView.as_view(), name='eliminar_libro'),

]
    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)