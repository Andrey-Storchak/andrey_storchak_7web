from django.contrib import admin

from apps.pynote.models import Note
from apps.pynote import forms


class NoteAdmin(admin.ModelAdmin):
    form = forms.NoteForm

admin.site.register(Note, NoteAdmin)
