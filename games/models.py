from urllib.parse import urlparse, parse_qs

from django.db import models
from django.core.validators import URLValidator
from tinymce.models import HTMLField

from utils.models import UUIDModel


class Game(UUIDModel):
    """Model of game

    Attributes
    ----------
    title : CharField
        Game title
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
    title = models.CharField('game title', max_length=255)
    preview = models.ImageField('game preview', upload_to='games')
    short_description = models.CharField(
        'game short description in English', max_length=1000
    )
    short_description_ru = models.CharField(
        'game short description in Russian', max_length=1000, blank=True
    )
    description = HTMLField('game description in English')
    description_ru = HTMLField('game description in Russian', blank=True)
    video = models.URLField(
        'game video link on youtube',
        validators=[
            URLValidator(regex=r"https://(?:www.)?youtube.com/watch.*v=.*",
                         message="A video link need to be from YouTube")
        ]
    )
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date', 'title')

    def __str__(self) -> str:
        return str(self.title)

    @property
    def video_widget_url(self) -> str:
        """Return URL for YouTube widget"""
        video_url = urlparse(self.video)
        queries = parse_qs(video_url.query)
        uri = f"https://www.youtube.com/embed/{queries['v'][0]}"
        return uri


class GameImage(models.Model):
    """Model of game's image

    Attributes
    ----------
    image : ImageField
        Game image
    game : ForeignKey[Game]
        Foreign key to Game

    """
    image = models.ImageField('game image', upload_to='games')
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='images',
        verbose_name='game'
    )
