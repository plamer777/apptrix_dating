"""This file contains classes representing User models in the Django admin
panel"""
from django.contrib import admin
from core.models import User
# --------------------------------------------------------------------------


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """This class serves to represent a User model in the Django admin panel"""
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email', 'is_active')
    search_fields = ('username', 'email')
