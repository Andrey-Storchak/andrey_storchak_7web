from django.test import TestCase
from django.template import Template, Context

from apps.pynote import models


class TestInclusionTag(TestCase):

    def setUp(self):
        self.note = models.Note.objects.create(title='Testing note',
                                               text='Testing text!')
        self.rendered_template = Template('''
            {% load get_note %}
            {% note_by_id 1 %}
            ''').render(Context())

    def test_tag(self):
        self.assertIn(self.note.title, self.rendered_template)
        self.assertIn(self.note.text, self.rendered_template)
