# Generated by Django 4.2.2 on 2023-06-25 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_blockeduser_friend_alter_blockeduser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockeduser',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_u', to=settings.AUTH_USER_MODEL),
        ),
    ]
