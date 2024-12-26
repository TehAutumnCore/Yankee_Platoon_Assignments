# Generated by Django 5.1.4 on 2024-12-23 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game_app', '0002_game_sale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libraries', to='game_app.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libraries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'libraries',
                'unique_together': {('user', 'game')},
            },
        ),
    ]