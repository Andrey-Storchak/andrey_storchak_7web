from django import template

from apps.pynote import models

register = template.Library()


@register.inclusion_tag('pynote/templates/note.html')
def note_by_id(note_id):
    try:
        note = models.Note.objects.get(pk=int(note_id))
        return {'note': note}
    except:
        return {}