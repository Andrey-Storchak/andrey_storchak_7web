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
                                    self.v_note_creds,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        created_note = models.Note.objects.get(pk=1)
        self.assertEqual(created_note.title,
                         self.v_note_creds['title'].upper())
        self.assertEqual(created_note.text,
                         self.v_note_creds['text'])
        self.assertIn('request_result', response.content)
        self.assertIn('Note added successfuly.', response.content)

    def test_invalid_add(self):
        response = self.client.post(reverse('add_note'),
                                    self.i_note_creds,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(models.Note.DoesNotExist):
            models.Note.objects.get(pk=1)
        self.assertIn('request_result', response.content)
        self.assertIn('Error occured.', response.content)

    def test_add_img(self):
        with open('testdata/test.jpg', 'r') as attach:
            v_data = self.v_note_creds.copy()
            v_data['attach'] = attach
            response = self.client.post(reverse('add_note'),
                                        v_data,
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertContains(response, 'success')

            response = self.client.get(reverse('home'))
            filename = attach.name.split('/')[1]
            self.assertIn(filename, response.content)


class TestUpperCharField(TestCase):

    def setUp(self):
        self.text = "some text in lowercase"

    def test_upper_field(self):
        field = form_fields.UpperCharField()
        self.assertEqual(self.text.upper(), field.clean(self.text))
