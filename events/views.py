from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import EventForm, SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


@login_required
def profil_view(request):
    user = request.user  # Récupère l'utilisateur actuellement connecté
    if user.role == 'organisateur':
        # Logique spécifique pour les organisateurs
        return render(request, 'organisateur_dashboard.html')
    else:
        # Logique pour les participants
        return render(request, 'participant_dashboard.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Crée un nouvel utilisateur et enregistre-le dans la base de données
            user = form.save(commit=False) #False pour ne pas l'enregistrer tout de suite a la base de donnée
            user.set_password(form.cleaned_data['password']) # cryptage du mot de passe
            user.save()

            # se connecter automatiquement après l'inscription
            login(request, user)

            #rediriger directement vers la page d'acceuil que je vais creer plus tard
    else :
        form = SignUpForm
    
    return render(request, 'signup.html', {'form': form})


# vue pour connextion

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue, {username} ! Vous êtes connecté.")
            return redirect('home')  # Redirige vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')

def logout_view (request) :
    logout(request)
    messages.success(request,'Vous etes deconnectés')
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # Associe l'utilisateur connecté comme organisateur
            event.save()
            return redirect('home')  # Redirige après création
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})