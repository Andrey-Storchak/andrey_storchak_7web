from django import forms


class UpperCharField(forms.CharField):
    '''CharField for keeping string in uppercase'''

    def clean(self, value):
        try:
            return value.upper()
        except:
            raise forms.ValidationError
