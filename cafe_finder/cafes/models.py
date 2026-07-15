from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cafe(models.Model):

    class BarrioChoices(models.TextChoices):
        PALERMO = 'PAL', 'Palermo'
        SAN_TELMO = 'STL', 'San Telmo'
        RECOLETA = 'REC', 'Recoleta'
        LA_BOCA = 'BOC', 'La Boca'
        BELGRANO = 'BEL', 'Belgrano'

    name = models.CharField(max_length=100)
    barrio = models.CharField(
        max_length=3,
        choices=BarrioChoices.choices,
        default=BarrioChoices.PALERMO
    )
    address = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    has_good_medialunas = models.BooleanField(default=False)

    class Meta:
        ordering = ['-rating', 'name']

    def __str__(self):
        return f"{self.name} ({self.barrio})"
    

class Barrio(models.Model):

    barrio_name = models.CharField(max_length=50,
                                   unique=True)
    comuna = models.IntegerField()
    # in models.py
    summary = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.barrio_name} Comuna ({self.comuna})"