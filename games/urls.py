from django.urls import path

from .views import GameView


urlpatterns = [
    path('<slug:slug>/', GameView.as_view(), name='game'),
]
