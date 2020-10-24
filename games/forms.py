from django import forms

from .models import Game


class GameForm(forms.ModelForm):
    short_description = forms.CharField(
        max_length=1000, widget=forms.Textarea,
        label='Game short description in English'
    )
    short_description_ru = forms.CharField(
        max_length=1000, widget=forms.Textarea, required=False,
        label='Game short description in Russian'
    )
