# Generated by Django 3.1.4 on 2021-01-13 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='category',
            new_name='role',
        ),
    ]
