# Generated by Django 5.0.3 on 2024-05-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name1',
        ),
        migrations.RemoveField(
            model_name='person',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='person',
            name='name3',
        ),
        migrations.AddField(
            model_name='person',
            name='amount',
            field=models.CharField(default='Default amount', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='loan',
            field=models.CharField(default='Default loan', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='payment',
            field=models.CharField(default='Default payment', max_length=100),
        ),
    ]