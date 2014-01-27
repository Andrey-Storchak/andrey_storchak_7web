from django import forms
from django.forms.util import ErrorList

from . import models
from . import form_fields


class NoteForm(forms.ModelForm):

    title = form_fields.UpperCharField(required=True,
                                       widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Note title'}))

    text = forms.CharField(min_length=8,
                widget=forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Note text'}
                    )
            )

    class Meta:
        model = models.Note
