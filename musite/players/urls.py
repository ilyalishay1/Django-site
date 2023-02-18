from django.urls import path
from players import views


urlpatterns = [
    path('', views.home, name='home'),
    path('players_now/', views.players_now, name='players_now'),
    path('all_time_players/', views.all_time_players, name='all_time_players'),
    path('new_post/', views.add_post, name='new_post'),
]
