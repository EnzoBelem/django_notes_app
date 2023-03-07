from django.contrib import admin

from .models import Note, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    ...
