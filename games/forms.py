from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Game


class GameForm(forms.ModelForm):
    short_description = forms.CharField(
        label=_('game short description in English'), widget=forms.Textarea
    )
    short_description_ru = forms.CharField(
        label=_('game short description in Russian'), widget=forms.Textarea,
        required=False
    )

    class Meta:
        model = Game
        fields = (
            'title', 'slug', 'preview', 'short_description',
            'short_description_ru', 'description', 'description_ru', 'video'
        )
