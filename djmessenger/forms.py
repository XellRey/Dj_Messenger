import datetime
from django import forms
from djmessenger.models import Message, File_message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('message',)
        date = datetime.datetime.now()


class FileForm(forms.ModelForm):
    class Meta:
        model = File_message
        fields = ('file',)



