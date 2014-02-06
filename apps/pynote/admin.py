from django.contrib import admin

from apps.pynote.models import Note
from apps.pynote.models import Book
from apps.pynote import forms


class NoteAdmin(admin.ModelAdmin):
    form = forms.NoteForm


class NoteInline(admin.TabularInline):
    model = Book.notes.through

class BookAdmin(admin.ModelAdmin):
    inlines = [ NoteInline, ]
    fields = ['book_name']


admin.site.register(Note, NoteAdmin)
admin.site.register(Book, BookAdmin)
