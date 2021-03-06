from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'reviews'

class Calificacion(models.Model):
    calificacion = models.CharField(max_length=255)

    def __str__(self):
        return self.calificacion

    class Meta:
        app_label = 'reviews'

class Nombre(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'reviews'

class Plataforma(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'reviews'

class Player(models.Model):
    numJugadores = models.CharField(max_length=255)

    def __str__(self):
        return self.numJugadores

    class Meta:
        app_label = 'reviews'

class Publisher(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'reviews'

class ESRB(models.Model):
    clasificacion = models.CharField(max_length=255)

    def __str__(self):
        return self.clasificacion
    
    class Meta:
        app_label = 'reviews'

class Serie(models.Model):
    serie = models.CharField(max_length=255)

    def __str__(self):
        return self.serie
    
    class Meta:
        app_label = 'reviews'

class General(models.Model):
    genero = models.ForeignKey(Genero)
    calificacion1 = models.IntegerField(default=777)
    calificacion2 = models.IntegerField(default=777)
    calificacion3 = models.IntegerField(default=777)
    calificacion4 = models.IntegerField(default=777)
    calificacion5 = models.IntegerField(default=777)
    calificacionP = models.IntegerField(default=777)
    nombre = models.ForeignKey(Nombre)
    plataforma = models.ForeignKey(Plataforma)
    player = models.ForeignKey(Player)
    publisher = models.ForeignKey(Publisher)
    esrb = models.ForeignKey(ESRB)
    fecha_lanzamiento = models.DateField()
    serie = models.ForeignKey(Serie, default=777)
    foto = models.ImageField(upload_to='assets/images')
    trailer = models.FileField(upload_to='assets/videos')
    resumen = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre.nombre
    
    class Meta:
        app_label = 'reviews'

