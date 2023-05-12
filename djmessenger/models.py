from django.db import models
from account.admin import CustomUser


# Create your models here.


class Message(models.Model):
    message = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
