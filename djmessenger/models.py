from django.db import models
from account.admin import CustomUser
# Create your models here.


class Message(models.Model):
    message = models.TextField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    msg_sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='msg_sender')
    msg_receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='msg_receiver')
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
