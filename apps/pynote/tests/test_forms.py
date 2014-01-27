from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.pynote import models
from apps.pynote import form_fields


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
        self.assertEqual(created_note.title,
                         self.v_note_creds['title'].upper())
        self.assertEqual(created_note.text,
                         self.v_note_creds['text'])

    def test_invalid_add(self):
        response = self.client.post(reverse('add_note'),
                                    self.i_note_creds)
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(models.Note.DoesNotExist):
            models.Note.objects.get(pk=1)


class TestUpperCharField(TestCase):

    def setUp(self):
        self.text = "some text in lowercase"

    def test_upper_field(self):
        field = form_fields.UpperCharField()
        self.assertEqual(self.text.upper(), field.clean(self.text))
