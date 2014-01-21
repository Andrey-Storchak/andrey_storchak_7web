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
        self.note = models.Note.objects.create(title='Testing note', text='Testint text!')
        self.template = Template('''
            {% load get_note %}
             {% get_note_by_id {note_id} %}
            '''.format(note_id=self.note.pk))

    def test_tag(self):
        self.assertIn(self.note.title, self.template.render(Context()))
        self.assertIn(self.note.text, self.template.render(Context()))