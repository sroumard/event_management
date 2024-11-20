from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def profil_view(request):
    user = request.user  # Récupère l'utilisateur actuellement connecté
    if user.role == 'organisateur':
        # Logique spécifique pour les organisateurs
        return render(request, 'organisateur_dashboard.html')
    else:
        # Logique pour les participants
        return render(request, 'participant_dashboard.html')