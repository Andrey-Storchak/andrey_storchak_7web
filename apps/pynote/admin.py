from django.contrib import admin

from apps.pynote.models import Note
from apps.pynote.models import Book
from apps.pynote import forms


class MemberShipInline(admin.TabularInline):
    model = Book.notes.through


class NoteAdmin(admin.ModelAdmin):
    inlines = [ MemberShipInline, ]


class BookAdmin(admin.ModelAdmin):
    inlines = [ MemberShipInline, ]
    exclude = ('notes', )


admin.site.register(Note, NoteAdmin)
admin.site.register(Book, BookAdmin)
