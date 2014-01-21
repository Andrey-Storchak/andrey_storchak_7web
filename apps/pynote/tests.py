from django.core.urlresolvers import reverse
from django.test import TestCase

from . import models


class TestHomeView(TestCase):
    def setUp(self):
        self.notes = models.Note.objects.all()

    def test_notes_display(self):
        home_page = self.client.get(reverse('home'))
        for note in self.notes:
            self.assertIn(note.title, home_page.content)
            self.assertIn(note.text, home_page.content)
