from django.contrib import admin
from .models import *


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'date', 'is_published', 'cat')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(PlayersModel, PlayersAdmin)
admin.site.register(Category)
