# Generated by Django 4.2.2 on 2023-06-17 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customuser_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='contact',
            new_name='contacts',
        ),
    ]