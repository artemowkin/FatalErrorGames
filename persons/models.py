from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import UUIDModel


class Person(UUIDModel):
    """Person model

    Attributes
    ----------
    avatar : ImageField
        Person avatar
    name : CharField
        Person name in English
    name_ru : CharField
        Person name in Russian
    profession : CharField
        Person profession in English
    profession_ru : CharField
        Person profession in Russian
    about : CharField
        Information about person in English
    about_ru : CharField
        Information about person in Russian

    """

    avatar = models.ImageField(_('person avatar'), upload_to='persons')
    name = models.CharField(_('person name in English'), max_length=255)
    name_ru = models.CharField(
        _('person name in Russian'), max_length=255, blank=True
    )
    profession = models.CharField(
        _('person profession in English'), max_length=255
    )
    profession_ru = models.CharField(
        _('person profession in Russian'), max_length=255, blank=True
    )
    about = models.CharField(
        _('information about person in English'), max_length=1000
    )
    about_ru = models.CharField(
        _('information about person in Russian'), max_length=1000, blank=True
    )

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self) -> str:
        return str(self.name)
