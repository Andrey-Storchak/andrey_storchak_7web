from django import template

from apps.pynote.models import Note

register = template.Library()


@register.inclusion_tag('pynote/templates/note.html')
def note_by_id(note_id):
    try:
        note = Note.objects.get(pk=int(note_id))
        return {'note': note}
    except:
        return {}
