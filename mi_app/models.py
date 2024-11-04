from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)        
    autor = models.CharField(max_length=200)         
    descripcion = models.TextField()                 
    fecha_publicacion = models.DateField()            
    imagen = models.ImageField(upload_to='libros/')    

    def __str__(self):
        return self.titulo



class Pagina(models.Model):
    titulo = models.CharField(max_length=100)  
    autor = models.CharField(max_length=50)  
    descripcion = models.TextField()  
    fecha = models.DateField(auto_now_add=True)  
    imagen = models.ImageField(upload_to='pages/', null=True, blank=True)  

    def __str__(self):
        return self.titulo
