# Generated by Django 5.1.4 on 2024-12-13 21:50

import user_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_user_age_user_display_name_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[user_app.validators.validate_email]),
        ),
    ]
