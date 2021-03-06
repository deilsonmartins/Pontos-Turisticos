from django.db import models

class Endereco(models.Model):
    linha1 = models.TextField(max_length=150)
    linha2 = models.TextField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
