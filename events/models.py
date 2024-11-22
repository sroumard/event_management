from django.contrib.auth.models import AbstractUser
from django.db import models

from event_management import settings

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

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.title

