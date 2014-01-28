from pynote.models import Note


def notes_count(request):
    '''Returns total count of notes in db'''
    count = Note.objects.count()
    return {'notes_count': count}
