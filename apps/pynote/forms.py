from django import forms
from . import models


class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'text': forms.TextInput(attrs={
                'class': 'form-control'
                })
        }

    def is_valid(self):
        parent_result = super(NoteForm, self).is_valid(self)
        if parent_result:
            self_result = len(self.cleaned_data['text']) > 8
            return parent_result == self_result
        else:
            self.erros['text'] = "Text must be more the 8 symbols."
            return parent_result
