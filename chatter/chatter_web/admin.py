from django.contrib import admin
from .models import Theme, Genre
# Register your models here.

admin.site.register(Genre)

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_filter = ['genre']
    search_fields = ('theme', 'genre')