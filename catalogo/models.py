from django.db import models

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    puntuacion = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.nombre

class Reseña(models.Model):
    juego = models.ForeignKey(Juego, related_name='reseñas', on_delete=models.CASCADE)
    texto = models.TextField()
    puntuacion = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"Reseña de {self.juego.nombre}"
