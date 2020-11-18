from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import UUIDModel
from langs.models import Language


class Person(UUIDModel):

    """Person model

    Attributes
    ----------
    avatar : ImageField
        Person avatar
    name : CharField
        Person name
    profession : CharField
        Person profession
    about : CharField
        Information about person
    language : ForeignKey
        Language of person

    """

    avatar = models.ImageField(_('person avatar'), upload_to='persons')
    name = models.CharField(_('person name'), max_length=255)
    profession = models.CharField(
        _('person profession'), max_length=255
    )
    about = models.CharField(
        _('information about person'), max_length=1000
    )
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, verbose_name=_('language')
    )

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self) -> str:
        return str(self.name)
