from django.urls import path
from . import views  # Importe les vues de ton application

urlpatterns = [
    
    path('signup/', views.sign_up, name='signup'),  # URL pour l'inscription
    path('login/', views.login_view, name ="login"),
    path('logout/', views.logout_view, name='logout'),  # Nouvelle route pour la déconnexion
    path('home/', views.home, name='home'), 
    path('events/create/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
    path('update-event/<int:event_id>/', views.update_event, name='update_event'),
    path('update-event/<int:event_id>/', views.delete_event, name='delete_event'),


]