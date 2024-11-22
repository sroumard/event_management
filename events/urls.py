from django.urls import path
from . import views  # Importe les vues de ton application

urlpatterns = [
    
    path('signup/', views.sign_up, name='signup'),  # URL pour l'inscription
    path('login/', views.login_view, name ="login"),
    path('logout/', views.logout_view, name='logout'),  # Nouvelle route pour la déconnexion
    path('home/', views.home, name='home'), 
    path('events/create/', views.create_event, name='create_event')
]