from django.contrib import admin

from . import models
from . import forms


class NoteAdmin(admin.ModelAdmin):
    form = forms.NoteForm

admin.site.register(models.Note, NoteAdmin)
