# Generated by Django 5.0.3 on 2024-05-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_medical_bp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='allergy',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='medical',
            name='asthma',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='medical',
            name='cholestrol',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='medical',
            name='diabetic',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='medical',
            name='thyroid',
            field=models.CharField(max_length=10),
        ),
    ]