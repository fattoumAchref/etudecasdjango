# Generated by Django 5.1.1 on 2024-10-12 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='titre',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Le titre doit contenir seulement des caractères.', regex='^[a-zA-Z\\s]+$')]),
        ),
    ]