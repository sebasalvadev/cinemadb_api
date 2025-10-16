from rest_framework import serializers
from .models import Director, Pelicula


class DirectorSerializer(serializers.ModelSerializer):
    
    cantidad_peliculas = serializers.SerializerMethodField()
    
    class Meta:
        model = Director
        fields = ['id', 'nombre', 'nacionalidad', 'fecha_nacimiento', 'cantidad_peliculas']
    
    def get_cantidad_peliculas(self, obj):
        return obj.peliculas.count()


class DirectorSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Director
        fields = ['id', 'nombre', 'nacionalidad']


class PeliculaSerializer(serializers.ModelSerializer):
    
    director_info = DirectorSimpleSerializer(source='director', read_only=True)
    
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(), write_only=True)
    
    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'genero', 'anio_estreno', 'director', 'director_info', 
                  'duracion_minutos', 'sinopsis']
    
    def to_representation(self, instance):
        
        representation = super().to_representation(instance)
        
        representation['director'] = representation.pop('director_info')
        return representation


class PeliculaListSerializer(serializers.ModelSerializer):
    
    director_nombre = serializers.CharField(source='director.nombre', read_only=True)
    
    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'genero', 'anio_estreno', 'director_nombre']
