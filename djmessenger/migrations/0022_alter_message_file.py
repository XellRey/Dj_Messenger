# Generated by Django 4.2.2 on 2023-06-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djmessenger', '0021_alter_message_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
