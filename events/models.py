from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Définir les choix pour le rôle
    ROLE_CHOICES = (
        ('organisateur', 'Organisateur'),
        ('participant', 'Participant'),
    )
    # Champ pour stocker le rôle de l'utilisateur
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='participant')

    def __str__(self):
        return f"{self.username} ({self.role})"
