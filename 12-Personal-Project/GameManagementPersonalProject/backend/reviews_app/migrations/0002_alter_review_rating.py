# Generated by Django 5.1.4 on 2024-12-26 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]