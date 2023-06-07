from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='media/', null=True)
    is_contact = models.BooleanField(default=False)
    username = models.CharField(unique=True)
    contact = models.ManyToManyField('Contact', related_name='my_contacts')


class Contact(models.Model):
    profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='all_contacts')

    def __str__(self):
        return self.profile.username
