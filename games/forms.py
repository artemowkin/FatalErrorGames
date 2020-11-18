from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Game


class GameForm(forms.ModelForm):
    short_description = forms.CharField(
        max_length=1000, widget=forms.Textarea,
        label=_('Game short description')
    )

    class Meta:
        model = Game
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        slug = cleaned_data['slug']
        language = cleaned_data['language']
        objects_count = self.Meta.model.objects.filter(
            slug=slug, language=language
        ).count()
        if objects_count > 0:
            raise forms.ValidationError(
                "The entry with the same `slug` and `language` already exists"
            )
