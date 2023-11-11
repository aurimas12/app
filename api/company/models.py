from django.db import models

# Create your models here.

class CompanyInfo(models.Model):
    
    CITY_CHOICES = [
        'Airijoje', 'Alytuje', 'Anykščiuose', 'Belgijoje', 'Birštone', 'Biržuose', 
        'Danijoje', 'Darbas namuose', 'Druskininkuose', 'Elektrėnuose', 'Gargžduose', 
        'Graikijoje', 'Islandijoje', 'Ispanijoje', 'JAV', 'Jonavoje', 'Joniškyje', 
        'Jungtiniuose Arabų Emiratuose', 'Jungtinėje Karalystėje', 'Jurbarke', 
        'Kaišiadoryse', 'Kalvarijoje', 'Kaune', 'Kazlų Rūdoje', 'Kelmėje', 'Kipre', 
        'Klaipėdoje', 'Kretingoje', 'Kupiškyje', 'Kuršėnuose', 'Kėdainiuose', 
        'Latvijoje', 'Lazdijuose', 'Lenkijoje', 'Lentvaryje', 'Marijampolėje', 
        'Mažeikiuose', 'Molėtuose', 'Naujojoje Akmenėje', 'Neringoje', 'Norvegijoje', 
        'Nyderlanduose', 'Pakruojyje', 'Palangoje', 'Panevėžyje', 'Pasvalyje', 'Plungėje', 
        'Prancūzijoje', 'Prienuose', 'Radviliškyje', 'Raseiniuose', 'Rietave', 'Rokiškyje', 
        'Suomijoje', 'Tauragėje', 'Telšiuose', 'Trakuose', 'Ukmergėje', 'Utenoje', 
        'Varėnoje', 'Vievyje', 'Vilkaviškyje', 'Vilniuje', 'Visagine', 'Vokietijoje', 
        'Zarasuose', 'Šakiuose', 'Šalčininkuose', 'Šiauliuose', 'Šilalėje', 'Šilutėje', 
        'Širvintose', 'Švedijoje'
    ]

    name = models.CharField(max_length=150, unique=True)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    logo_url = models.URLField(max_length=200, blank=True, null=True)
 