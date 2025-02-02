# Generated by Django 5.1.4 on 2024-12-13 21:29

import django.core.validators
import user_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=18, validators=[django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(unique=True, validators=[user_app.validators.validate_email]),
        ),
    ]
