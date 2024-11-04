from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='libro_list'),
    path('libros/create/', views.crear_libro, name='libro_create'),
    path('libros/update/<int:pk>/', views.libro_update, name='libro_update'),
    path('libros/delete/<int:pk>/', views.libro_delete, name='libro_delete'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pages/', views.lista_libros, name='lista_libros'),
    path('pages/create/', views.crear_pagina, name='crear_pagina'),
    path('pages/<int:pk>/edit/', views.update_page, name='update_page'),
    path('pages/<int:pk>/delete/', views.delete_page, name='delete_page'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]
