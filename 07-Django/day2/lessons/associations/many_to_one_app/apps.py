from django.apps import AppConfig


class ManyToOneAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'many_to_one_app'