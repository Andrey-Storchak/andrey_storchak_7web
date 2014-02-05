from django.db import models
from django.db.models import signals
from django.dispatch import receiver


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


class Book(models.Model):
    '''Model to store notes'''

    book_name = models.CharField(max_length=255,
                                                          verbose_name=u"Book name")
    notes = models.ManyToManyField(Note)


    def __unicode__(self):
        '''Unicode representation of Book object'''

        return unicode(self.book_name)



#-------------------------------------------------------------------------------------#
#                           Signals processors                                         #
#-------------------------------------------------------------------------------------#

@receiver(signals.pre_delete, sender=Note)
def note_predelete_handler(sender, **kwargs):
    for book in kwargs['instance'].book_set.all():
        if book.notes.count() == 1:
            book.delete()
