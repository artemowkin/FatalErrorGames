from django.urls import path
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='news/'), name='redirect'),
    path(
        'news/', TemplateView.as_view(template_name='news.html'),
        name='news'
    ),
    path(
        'cooperation/',
        TemplateView.as_view(template_name='cooperation.html'),
        name='cooperation'
    ),
]
