from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.pynote import models


class TestHomeView(TestCase):
    fixtures = ['db_data.json']

    def setUp(self):
        self.notes = models.Note.objects.all()

    def test_notes_display(self):
        home_page = self.client.get(reverse('home'))
        for note in self.notes:
            self.assertIn(note.title, home_page.content)
            self.assertIn(note.text, home_page.content)

class TestWidgetView(TestCase):

    def setUp(self):
        self.created_note = models.Note.objects.create(title="TEST", text="TEST TEXT")

    def test_widget(self):
        response = self.client.get(reverse('widget'))
        self.assertIn(self.created_note.title, response.content)
        self.assertIn(self.created_note.text, response.content)
