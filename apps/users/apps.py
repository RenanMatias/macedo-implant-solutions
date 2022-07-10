from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self, *args, **kwargs) -> None:
        import apps.users.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
