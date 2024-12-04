from django.urls import path
from .views import (
    home, about, signup, profile, login_view, logout_view, buscar_libro,
    CrearLibroView, ListaLibroView, ActualizarLibroView, EliminarLibroView
)

from django.conf import settings


from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import change_password
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('buscar/', buscar_libro, name='buscar_libro'),
    path('accounts/password_change/', change_password, name='password_change'),
    path('page/<int:pk>/', views.page_detail, name='page_detail'),
    path('page/<int:pk>/edit/', views.page_edit, name='page_edit'),
     path('page/<int:pk>/edit/', views.page_edit, name='page_edit'),
   
  
    #  CRUD CON CBV
    path('libros/', ListaLibroView.as_view(), name='lista_libro'),
    path('libros/crear/', CrearLibroView.as_view(), name='crear_libro'),
    path('libros/<int:pk>/editar/', ActualizarLibroView.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', EliminarLibroView.as_view(), name='libro_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)