# Generated by Django 4.2.1 on 2023-06-01 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djmessenger', '0006_alter_message_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='userid',
        ),
    ]
