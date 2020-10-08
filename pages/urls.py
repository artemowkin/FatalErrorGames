from django.urls import path, register_converter

from .views import NewsView, CooperationView, RedirectView
from utils.urls import LanguageConverter


register_converter(LanguageConverter, 'language')

urlpatterns = [
    path('', RedirectView.as_view(), name='redirect'),
    path('<language:lang>/news/', NewsView.as_view(), name='news'),
    path(
        '<language:lang>/cooperation/',
        CooperationView.as_view(), name='cooperation'
    ),
]
