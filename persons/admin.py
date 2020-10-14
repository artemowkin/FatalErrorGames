from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'about')
    search_fields = ('name', 'profession', 'about')
