# Generated by Django 5.1.3 on 2024-11-14 15:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=1)),
                ('date_encountered', models.DateField(verbose_name='2015-01-01')),
                ('date_capture', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='Unknown')),
                ('captured', models.BooleanField(default=False)),
            ],
        ),
    ]
