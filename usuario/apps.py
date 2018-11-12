from django.apps import AppConfig

class UserProfileConfig(AppConfig):
    name = "profiles"
    verbose_name = 'User Profiles'

    def ready(self):
        from .models import create_profile_handler
 
