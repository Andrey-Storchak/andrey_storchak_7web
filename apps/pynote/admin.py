from django.contrib import admin

from apps.pynote.models import Note
from apps.pynote.models import Book
from apps.pynote import forms


class NoteAdmin(admin.ModelAdmin):
    form = forms.NoteForm


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)
admin.site.register(Book, BookAdmin)
