# Generated by Django 4.2.2 on 2023-06-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djmessenger', '0015_alter_message_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]