from django.db import models

# Create your models here.
class Feedback(models.Model):
    te_gusta_la_pagina = models.CharField(max_length=2)  # "Si" o "No"
    genero_musical = models.CharField(max_length=10)     # Ej. "Pop", "Rock", "Jazz"
    frecuencia_escucha = models.CharField(max_length=15) # Ej. "Diariamente", "Semanalmente"
    plataforma_utilizada = models.CharField(max_length=10)  # Ej. "Spotify", "YouTube"
    aprender_mas_musica = models.CharField(max_length=2)    # "Si" o "No"

    def __str__(self):
        return f"Feedback: {self.te_gusta_la_pagina}, {self.genero_musical}, {self.frecuencia_escucha}, {self.plataforma_utilizada}, {self.aprender_mas_musica}"