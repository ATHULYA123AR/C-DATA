# Generated by Django 5.0.3 on 2024-05-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='Passoutyear3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='education',
            name='Score3',
            field=models.IntegerField(default=0),
        ),
    ]
