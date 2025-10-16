from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
    
    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    GENEROS = [
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('romance', 'Romance'),
        ('suspenso', 'Suspenso'),
        ('animacion', 'Animación'),
    ]
    
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=50, choices=GENEROS)
    anio_estreno = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='peliculas')
    duracion_minutos = models.IntegerField(null=True, blank=True)
    sinopsis = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['-anio_estreno']
    
    def __str__(self):
        return f"{self.titulo} ({self.anio_estreno})"