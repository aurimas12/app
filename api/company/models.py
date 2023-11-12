from django.db import models


class Company(models.Model):
    
    VILNIUS = 1
    KAUNAS = 2
    KLAIPEDA = 3
    SIAULIAI = 4
    PANEVEZYS = 5
    
    CITY_CHOICES = (
        (VILNIUS, ('Vilnius')),
        (KAUNAS, ('Kaunas')),
        (KLAIPEDA, ('Klaipėda')), 
        (SIAULIAI, ('Šiauliai')), 
        (PANEVEZYS, ('Panevėžys')),
    )

    name = models.CharField(max_length=150, unique=True)
    city = models.PositiveSmallIntegerField(choices=CITY_CHOICES)
    logo_url = models.URLField(max_length=200, blank=True, null=True)
    