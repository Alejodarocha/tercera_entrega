from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)        
    autor = models.CharField(max_length=200)         
    descripcion = models.TextField()                 
    fecha_publicacion = models.DateField()            
    imagen = models.ImageField(upload_to='libros/')    

    def __str__(self):
        return self.titulo



class Page(models.Model):
    titulo = models.CharField(max_length=100)  
    autor = models.CharField(max_length=50)  
    descripcion = models.TextField()  
    fecha = models.DateTimeField(null=True)
    imagen = models.ImageField(upload_to='pages/', null=True, blank=True)  

    def __str__(self):
        return self.titulo

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, blank=True)
    imagen = models.ImageField(upload_to='profile_images', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'


from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
