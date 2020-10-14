from django.urls import path

from .views import GameView


urlpatterns = [
    path('<uuid:pk>/', GameView.as_view(), name='game'),
]
