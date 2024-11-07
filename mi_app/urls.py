from django.urls import path
from . import views
from django.contrib import admin
from .views import lista_libro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('', views.home, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pages/', lista_libro, name='lista_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
    path('libro_delete/<int:pk>/', views.libro_delete, name='libro_delete'),
    path('crear-libro/', views.crear_libro, name='crear_libro'),
    ]
