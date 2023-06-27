"""This file contains classes representing Client models in the Django admin
panel"""
from django.contrib import admin
from participant.models import Client
# --------------------------------------------------------------------------


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    """This class serves to represent a Client model in the Django admin
    panel"""
    list_display = ('email', 'first_name', 'last_name', 'gender')
    list_filter = ('email', 'gender')
    search_fields = ('email', )
