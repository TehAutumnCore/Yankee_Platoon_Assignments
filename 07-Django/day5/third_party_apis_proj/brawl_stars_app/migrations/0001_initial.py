# Generated by Django 5.1.3 on 2024-11-19 22:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brawler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brawler_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(16000000), django.core.validators.MaxValueValidator(16000087)])),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
