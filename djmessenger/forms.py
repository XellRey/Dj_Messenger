import datetime
from django import forms
from djmessenger.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('message', 'file')
        date = datetime.datetime.now()
        widgets = {
            'message': forms.Textarea(attrs={
                'oninput': 'checkTextLength()',
            }
            ),
            'file': forms.FileInput(attrs={})

        }


