from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    twitter_username = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posiciones_campo = (
        ('defensa', 'Defensa'),
        ('delantero', 'Delantero'),
        ('arquero', 'Arquero'),
        ('centro', 'Centro'),
        )
    posicion_campo = models.CharField(max_length=50, choices=posiciones_campo)
    numero_camiseta = models.PositiveIntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    nombre_auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_campeonato


class CampeonatoEquipos(models.Model):
    year = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} - {self.equipo.nombre}: {self.campeonato.nombre_campeonato}"
