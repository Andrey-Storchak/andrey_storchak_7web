from . import models


def notes_count(request):
    count = models.Note.objects.count()
    return {'notes_count': count}
