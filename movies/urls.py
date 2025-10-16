from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DirectorViewSet, PeliculaViewSet

router = DefaultRouter()
router.register(r'directores', DirectorViewSet, basename='director')
router.register(r'peliculas', PeliculaViewSet, basename='pelicula')

urlpatterns = [
    path('', include(router.urls)),
]