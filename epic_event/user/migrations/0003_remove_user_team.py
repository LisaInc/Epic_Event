# Generated by Django 4.0.5 on 2022-07-15 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='team',
        ),
    ]