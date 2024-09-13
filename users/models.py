from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Acheteur'),
        ('seller', 'Vendeur'),
        ('admin', 'Administrateur'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

class Annonce(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='annonces/', blank=True, null=True, default='/default/image.png')  # Chemin vers l'image par défaut
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Commande(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('completed', 'Complétée'),
        ('canceled', 'Annulée'),
    ]
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Commande pour {self.annonce.title} par {self.buyer.username}"
