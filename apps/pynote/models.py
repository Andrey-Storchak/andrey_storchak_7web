from django.db import models


class Note(models.Model):
    '''Model to store notes'''

    title = models.CharField(max_length=255,
                             verbose_name=u'Title')
    text = models.TextField(verbose_name='Note text')
    attach = models.ImageField(blank=True,
                               null=True,
                               upload_to="user_uploads/")

    def __unicode__(self):
        ''' Unicode representation of Note object'''

        return unicode(self.title)
