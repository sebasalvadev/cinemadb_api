from django.core.management.base import BaseCommand
from movies.models import Director, Pelicula
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        Pelicula.objects.all().delete()
        Director.objects.all().delete()
        
        directores_data = [
            {'nombre': 'Christopher Nolan', 'nacionalidad': 'Británico', 'fecha_nacimiento': date(1970, 7, 30)},
            {'nombre': 'Quentin Tarantino', 'nacionalidad': 'Estadounidense', 'fecha_nacimiento': date(1963, 3, 27)},
            {'nombre': 'Martin Scorsese', 'nacionalidad': 'Estadounidense', 'fecha_nacimiento': date(1942, 11, 17)},
            {'nombre': 'Steven Spielberg', 'nacionalidad': 'Estadounidense', 'fecha_nacimiento': date(1946, 12, 18)},
            {'nombre': 'Guillermo del Toro', 'nacionalidad': 'Mexicano', 'fecha_nacimiento': date(1964, 10, 9)},
        ]
        
        directores = []
        for data in directores_data:
            director = Director.objects.create(**data)
            directores.append(director)
            self.stdout.write(self.style.SUCCESS(f'Director creado: {director.nombre}'))
        
        peliculas_data = [
            {'titulo': 'Inception', 'genero': 'ciencia_ficcion', 'anio_estreno': 2010, 'director': directores[0], 'duracion_minutos': 148},
            {'titulo': 'The Dark Knight', 'genero': 'accion', 'anio_estreno': 2008, 'director': directores[0], 'duracion_minutos': 152},
            {'titulo': 'Pulp Fiction', 'genero': 'drama', 'anio_estreno': 1994, 'director': directores[1], 'duracion_minutos': 154},
            {'titulo': 'Kill Bill Vol. 1', 'genero': 'accion', 'anio_estreno': 2003, 'director': directores[1], 'duracion_minutos': 111},
            {'titulo': 'The Wolf of Wall Street', 'genero': 'comedia', 'anio_estreno': 2013, 'director': directores[2], 'duracion_minutos': 180},
            {'titulo': 'Goodfellas', 'genero': 'drama', 'anio_estreno': 1990, 'director': directores[2], 'duracion_minutos': 146},
            {'titulo': 'Jurassic Park', 'genero': 'ciencia_ficcion', 'anio_estreno': 1993, 'director': directores[3], 'duracion_minutos': 127},
            {'titulo': "Schindler's List", 'genero': 'drama', 'anio_estreno': 1993, 'director': directores[3], 'duracion_minutos': 195},
            {'titulo': 'El Laberinto del Fauno', 'genero': 'terror', 'anio_estreno': 2006, 'director': directores[4], 'duracion_minutos': 118},
            {'titulo': 'The Shape of Water', 'genero': 'romance', 'anio_estreno': 2017, 'director': directores[4], 'duracion_minutos': 123},
        ]
        
        for data in peliculas_data:
            pelicula = Pelicula.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Película creada: {pelicula.titulo}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Base de datos poblada exitosamente!'))
        self.stdout.write(self.style.SUCCESS(f'   - {Director.objects.count()} directores'))
        self.stdout.write(self.style.SUCCESS(f'   - {Pelicula.objects.count()} películas'))