from urllib.parse import urlparse, parse_qs

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator
from tinymce.models import HTMLField


class Game(models.Model):
    """Game model

    Attributes
    ----------
    title : CharField
        Game title
    slug: SlugField
        Game slug
    preview : ImageField
        Game preview image
    short_description : CharField
        Game short description in English
    short_description_ru : CharField
        Game short description in Russian
    description : HTMLField
        Game description in English
    description_ru : HTMLField
        Game description in Russian
    video : URLField
        Game video YouTube link
    pub_date : DateField
        Date published

    """
    title = models.CharField(_('game title'), max_length=255)
    slug = models.SlugField(_('game slug'), unique=True)
    preview = models.ImageField(
        _('game preview'), upload_to='games',
        help_text=_('preferably 1000x225 px')
    )
    short_description = models.CharField(
        _('game short description in English'), max_length=1000
    )
    short_description_ru = models.CharField(
        _('game short description in Russian'), max_length=1000, blank=True
    )
    description = HTMLField(_('game description in English'))
    description_ru = HTMLField(_('game description in Russian'), blank=True)
    video = models.URLField(
        _('game video link on youtube'),
        validators=[
            URLValidator(regex=r"https://(?:www\.)?youtube\.com/watch\?v=.*",
                         message="A video link need to be from YouTube")
        ]
    )
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date', 'title')
        verbose_name = _('game')
        verbose_name_plural = _('games')

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self) -> str:
        return reverse('game', args=[str(self.slug)])

    @property
    def video_widget_url(self) -> str:
        """Return URL for YouTube widget"""
        if not hasattr(self, '_video_widget_url'):
            video_url = urlparse(self.video)
            queries = parse_qs(video_url.query)
            url = f"https://www.youtube.com/embed/{queries['v'][0]}"
            self._video_widget_url = url

        return self._video_widget_url


class GameImage(models.Model):
    """Model of game image

    Attributes
    ----------
    image : ImageField
        Game image
    game : ForeignKey[Game]
        Foreign key to Game

    """
    image = models.ImageField(_('game image'), upload_to='games')
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='images',
        verbose_name=_('game')
    )

    class Meta:
        verbose_name = _('game image')
        verbose_name_plural = _('game images')
