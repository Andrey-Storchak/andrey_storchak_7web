from django import forms
from django.forms.util import ErrorList

from . import models
from . import form_fields


class NoteForm(forms.ModelForm):

    title = form_fields.UpperCharField(required=True,
                                       widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Note title'}))

    class Meta:
        model = models.Note
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Note text'})}

    def is_valid(self):
        parent_result = super(NoteForm, self).is_valid()
        if parent_result:
            self_result = len(self.cleaned_data['text']) > 8
            if parent_result == self_result:
                return True
            else:
                text_errors = self._errors.setdefault('text', ErrorList())
                text_errors.append(u"Text must be more then 8 symbols.")
                return False
        return False
