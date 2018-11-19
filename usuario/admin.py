from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from django.contrib.auth.models import User


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
