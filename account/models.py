from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/', default='default/no-avatar.png')
    is_contact = models.BooleanField(default=False)
    username = models.CharField(unique=True)
    description = models.CharField(max_length=70, null=True, blank=True)
    blocked_list = models.ManyToManyField('BlockedUser', related_name='blocked_users')


class ContactList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friends')

    @staticmethod
    def add_friend(user, new_friend):
        contact_list, created = ContactList.objects.get_or_create(
            user=user
        )
        contact_list.user.add(new_friend)


class BlockedUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='block_u')

    def __str__(self):
        return self.user.username

    @staticmethod
    def block_users(user, block_u):
        block_list, created = BlockedUser.objects.get_or_create(
            user=user
        )
        block_list.user.block(block_u)

    @staticmethod
    def unblock_users(user, block_u):
        block_list, created = BlockedUser.objects.get_or_create(
            user=user
        )
        block_list.user.block(block_u)
