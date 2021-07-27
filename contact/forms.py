from django import forms
from .models import UserMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = '__all__'

