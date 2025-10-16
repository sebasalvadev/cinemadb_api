from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Director, Pelicula
from .serializers import DirectorSerializer, PeliculaSerializer, PeliculaListSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre', 'nacionalidad']
    
    @action(detail=True, methods=['get'])
    def peliculas(self, request, pk=None):
        director = self.get_object()
        peliculas = director.peliculas.all()
        serializer = PeliculaListSerializer(peliculas, many=True)
        return Response(serializer.data)


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.select_related('director').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo', 'genero']
    filterset_fields = ['genero', 'anio_estreno', 'director']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PeliculaListSerializer
        return PeliculaSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        titulo = instance.titulo
        self.perform_destroy(instance)
        return Response(
            {"message": f"Película '{titulo}' eliminada exitosamente"},
            status=status.HTTP_200_OK
        )
