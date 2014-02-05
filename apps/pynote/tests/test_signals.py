from django.test import TestCase

from apps.pynote import models


class TestBookModel(TestCase):

    def setUp(self):
        self.created_book = models.Book.objects.create(book_name="Example")
        self.created_note = models.Note.objects.create(title="test", text="text")
        self.created_book.notes.add(self.created_note)

    def test_last_deletion(self):
        self.created_note.delete()
        with self.assertRaises(models.Book.DoesNotExist):
            models.Book.objects.get()

