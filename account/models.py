from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/', default='default/no-avatar.png')
    is_contact = models.BooleanField(default=False)
    username = models.CharField(unique=True)
    description = models.CharField(max_length=70, null=True, blank=True)
    contacts = models.ManyToManyField('Contact', related_name='my_contacts')
    blocked_list = models.ManyToManyField('BlockedUser', related_name='blocked_users')


class Contact(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default='0', blank=True)
    profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='all_contacts')

    def __str__(self):
        return self.profile.username

    @staticmethod
    def add_friend(profile, new_friend):
        contacts, created = Contact.objects.get_or_create(
            profile=profile
        )
        contacts.user.add(new_friend)


class BlockedUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='blocked_users_list')

    def __str__(self):
        return self.user.username

    def block_users(self):
        pass
