from django.core.urlresolvers import reverse
from django.template import Template, Context

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

class TestInclusionTag(TestCase):
    def setUp(self):
        self.note = models.Note.objects.create(title='Testing note', text='Testing text!')
        self.rendered_template = Template('''
            {% load get_note %}
            {% note_by_id 1 %}
            ''').render(Context())

    def test_tag(self):
        self.assertIn(self.note.title, self.rendered_template)
        self.assertIn(self.note.text, self.rendered_template)
