# Generated by Django 5.0.3 on 2024-05-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_eduform'),
    ]

    operations = [
        migrations.CreateModel(
            name='personform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Pincode', models.IntegerField()),
            ],
        ),
    ]
