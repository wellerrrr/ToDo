# Generated by Django 5.0.4 on 2024-05-25 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todolist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='user',
        ),
    ]