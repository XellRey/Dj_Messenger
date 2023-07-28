from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# User_Model
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/', default='default/no-avatar.png')
    is_contact = models.BooleanField(default=False)
    username = models.CharField(unique=True)
    description = models.CharField(max_length=70, null=True, blank=True)


# Contact_List_Model
class ContactList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friends')


# Blocked_User_List_Model
class BlockedUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='block_u')

    def __str__(self):
        return self.friend.username


