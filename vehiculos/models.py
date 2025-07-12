from django.db import models
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    placas = models.CharField(max_length=20)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"{self.placas} ({self.lat}, {self.lon})"
