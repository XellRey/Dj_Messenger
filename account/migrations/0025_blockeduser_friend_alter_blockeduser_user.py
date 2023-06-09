# Generated by Django 4.2.2 on 2023-06-25 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_alter_contactlist_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockeduser',
            name='friend',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='block_u', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blockeduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
