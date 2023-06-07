import datetime
from django import forms
from djmessenger.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('message',)
        date = datetime.datetime.now()


