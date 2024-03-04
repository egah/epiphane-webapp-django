from django import forms
from django.core import validators


class Message(forms.Form):
    text = forms.CharField(max_length=250, widget=forms.Textarea, label="Message")
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )
