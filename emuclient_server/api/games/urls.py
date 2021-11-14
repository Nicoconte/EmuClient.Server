from django.urls import path, include

from .views import *

urlpatterns = [
    path('create/', create_game_catalogue),
    path('list/', filter_games_by_catalogue),
    path('all/', list_games),
    path('all/catalogue/', list_games_catalogue)
]
