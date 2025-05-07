from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
from rest_framework.decorators import action
from .models import Juego, Desarrollador, Plataforma, Genero, Reseña
from .serializers import JuegoSerializer, DesarrolladorSerializer, PlataformaSerializer, GeneroSerializer, ReseñaSerializer

# Filtros personalizados para los juegos
class JuegoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')  # Filtrar por nombre del juego
    genero = django_filters.CharFilter(field_name='genero__nombre', lookup_expr='icontains')  # Filtrar por género
    desarrollador = django_filters.CharFilter(field_name='desarrollador__nombre', lookup_expr='icontains')  # Filtrar por desarrollador
    min_puntuacion = django_filters.NumberFilter(field_name='puntuacion', lookup_expr='gte')  # Filtrar por puntuación mínima
    max_puntuacion = django_filters.NumberFilter(field_name='puntuacion', lookup_expr='lte')  # Filtrar por puntuación máxima
    fecha_lanzamiento = django_filters.DateFilter(field_name='fecha_lanzamiento', lookup_expr='gte')  # Filtrar por fecha de lanzamiento

    class Meta:
        model = Juego
        fields = ['nombre', 'genero', 'desarrollador', 'min_puntuacion', 'max_puntuacion', 'fecha_lanzamiento']

# ViewSets para cada modelo

class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    filter_backends = (filters.OrderingFilter, django_filters.DjangoFilterBackend)
    filterset_class = JuegoFilter
    ordering_fields = ['nombre', 'puntuacion', 'fecha_lanzamiento']  # Se puede ordenar por estos campos
    ordering = ['nombre']  # Orden predeterminado por nombre

    # Endpoint para obtener los juegos mejor puntuados
    @action(detail=False, methods=['get'])
    def mejor_puntuacion(self, request):
        juegos = Juego.objects.order_by('-puntuacion')[:10]  # Obtenemos los 10 juegos mejor puntuados
        serializer = JuegoSerializer(juegos, many=True)
        return Response(serializer.data)


class DesarrolladorViewSet(viewsets.ModelViewSet):
    queryset = Desarrollador.objects.all()
    serializer_class = DesarrolladorSerializer


class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class ReseñaViewSet(viewsets.ModelViewSet):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer
