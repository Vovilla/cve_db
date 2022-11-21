from django.apps import AppConfig


class BaseManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_manager'
