from django.db import models

from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    """Language model

    Attributes
    ----------
    code : CharField
        Language code

    """
    code = models.CharField(_('language code'), max_length=2, unique=True)

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    def __str__(self) -> str:
        return self.code
