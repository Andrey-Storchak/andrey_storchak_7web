from django import forms


class UpperCharField(forms.CharField):

    def clean(self, value):
        try:
            return value.upper()
        except:
            raise forms.ValidationError
