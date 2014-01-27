from django.core.urlresolvers import reverse

from django.test import TestCase

from apps.pynote import models


class TestContext(TestCase):
    fixtures = ['db_data.json']

    def test_notes_count(self):
        count = models.Note.objects.count()
        response = self.client.get(reverse('home'))
        self.assertEqual(count, response.context['notes_count'])
