from rest_framework import serializers
from .models import Juego, Desarrollador, Plataforma, Genero, Reseña

class DesarrolladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollador
        fields = '__all__'

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class JuegoSerializer(serializers.ModelSerializer):
    desarrollador = DesarrolladorSerializer()
    plataforma = PlataformaSerializer()
    genero = GeneroSerializer()

    class Meta:
        model = Juego
        fields = '__all__'

class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseña
        fields = '__all__'
