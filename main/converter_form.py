from django import forms

class ConverterForm(forms.Form):
    valueToConvert = forms.CharField(label='Value to convert', max_length=100)