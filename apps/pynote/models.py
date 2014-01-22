from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255,
                             default='Note title',
                             verbose_name=u'Title')
    text = models.TextField(verbose_name='Note text')

    def __unicode__(self):
        return unicode(self.title)
