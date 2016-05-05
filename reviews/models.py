from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    calificacion = models.CharField(max_length=255)

    def __str__(self):
        return self.calificacion

class Nombre(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Player(models.Model):
    numJugadores = models.CharField(max_length=255)

    def __str__(self):
        return self.numJugadores

class Publisher(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class ESRB(models.Model):
    clasificacion = models.CharField(max_length=255)

    def __str__(self):
        return self.clasificacion

class Serie(models.Model):
    serie = models.CharField(max_length=255)

    def __str__(self):
        return self.serie

class General(models.Model):
    genero = models.ForeignKey(Genero)
    calificacion = models.ForeignKey(Calificacion)
    nombre = models.ForeignKey(Nombre)
    plataforma = models.ForeignKey(Plataforma)
    player = models.ForeignKey(Player)
    publisher = models.ForeignKey(Publisher)
    esrb = models.ForeignKey(ESRB)
    fecha_lanzamiento = models.DateField()
    serie = models.ForeignKey(Serie)
    foto = models.ImageField(upload_to='images')
    trailer = models.FileField(upload_to='videos')
    resumen = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre