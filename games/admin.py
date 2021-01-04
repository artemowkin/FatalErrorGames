from django.contrib import admin

from .models import Game, GameImage
from .forms import GameForm


class GameImageInline(admin.TabularInline):
    model = GameImage


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    form = GameForm
    inlines = [GameImageInline]
    list_display = ('title', 'pub_date', 'short_description')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ['title']}
