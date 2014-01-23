from django.core.urlresolvers import reverse
from django.template import Template, Context

from django.test import TestCase

from . import models


class TestHomeView(TestCase):
    fixtures = ['db_data.json']

    def setUp(self):
        self.notes = models.Note.objects.all()

    def test_notes_display(self):
        home_page = self.client.get(reverse('home'))
        for note in self.notes:
            self.assertIn(note.title, home_page.content)
            self.assertIn(note.text, home_page.content)


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


class TestAdditionForm(TestCase):

    def setUp(self):
        self.v_note_creds = {'title': 'Test note',
                             'text': 'Test text! more than 10 chars'}
        self.i_note_creds = {'title': 'Nt',
                             'text': 'small'}

    def test_valid_add(self):
        response = self.client.post(reverse('add_note'),
                                    self.v_note_creds)
        self.assertRedirects(response, reverse('home'), 302, 200)

        created_note = models.Note.objects.get(pk=1)
        self.assertEqual(created_note.title, self.v_note_creds['title'])
        self.assertEqual(created_note.text, self.v_note_creds['text'])

    def test_invalid_add(self):
        response = self.client.post(reverse('add_note'),
                                    self.i_note_creds)
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(models.Note.DoesNotExist):
            models.Note.objects.get(pk=1)
