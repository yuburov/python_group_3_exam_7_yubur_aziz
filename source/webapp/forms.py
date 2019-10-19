from django import forms
from webapp.models import Poll, Choise

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []


class ChoiseForm(forms.ModelForm):
    class Meta:
        model = Choise
        exclude = []

class PollChoiseForm(forms.ModelForm):
    class Meta:
        model = Choise
        fields = ['text']

