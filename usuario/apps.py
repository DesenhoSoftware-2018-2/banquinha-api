from django.apps import AppConfig

class UserProfileConfig(AppConfig):
    name = "profiles"
    verbose_name = 'Profiles'

    def ready(self):
        from .models import create_user_profile
        from .models import save_user_profile
