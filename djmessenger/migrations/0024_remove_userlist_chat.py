# Generated by Django 4.2.2 on 2023-07-20 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djmessenger', '0023_userlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlist',
            name='chat',
        ),
    ]
