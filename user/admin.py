from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from user.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = 'username', 'status', 'email', 'is_superuser',
