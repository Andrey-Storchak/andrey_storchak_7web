from django import forms
from . import models


class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Note title'
                }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Note text'
                })
        }

    def is_valid(self):
        parent_result = super(NoteForm, self).is_valid()
        if parent_result:
            self_result = len(self.cleaned_data['text']) > 8
            if parent_result == self_result:
                return True
            else:
                self.errors['text'] = "Text must be more then 8 symbols."
                return False
        return False
