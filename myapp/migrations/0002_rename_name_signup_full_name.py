# Generated by Django 5.0.3 on 2024-05-20 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='Name',
            new_name='Full_Name',
        ),
    ]
