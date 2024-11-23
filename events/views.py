from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Event
from .forms import EventForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@login_required
def profil_view(request):
    user = request.user  # Récupère l'utilisateur actuellement connecté
    if user.role == 'organisateur':
        return render(request, 'organisateur_dashboard.html')
    else:
        return render(request, 'participant_dashboard.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Crée un utilisateur sans l'enregistrer immédiatement
            user.set_password(form.cleaned_data['password'])  # Cryptage du mot de passe
            user.save()

            # Connecter automatiquement l'utilisateur après l'inscription
            login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil après inscription
    else:
        form = SignUpForm()  # Création d'un formulaire vide

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue, {username} ! Vous êtes connecté.")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté.')
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


@login_required
def event_list(request):
    # Récupération des filtres depuis la requête GET
    title_filter = request.GET.get('title', '')  # Mot-clé pour le titre
    date_filter = request.GET.get('date','' )
    location_filter = request.GET.get('location', '')  # Lieu

    events = Event.objects.all()  # Correction de la faute de frappe
    if title_filter:
        events = events.filter(title__icontains=title_filter)  # Recherche partielle insensible à la casse
    if date_filter :
        events = events.filter(date=date_filter)
    if location_filter:
        events = events.filter(location__icontains=location_filter)  # Recherche partielle sur la localisation
    
    return render(request, "events/event_list.html", {'events': events, 'filters': {
            'title': title_filter,
            'date': date_filter,
            'location': location_filter,
        },
        })


@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)  # Correction : utiliser l'objet existant
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm(instance=event)  # Pré-remplir le formulaire avec les données actuelles
    return render(request, "events/update_event.html", {'form': form})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect("event_list")
    return render(request, 'events/delete_event.html', {'event': event})
