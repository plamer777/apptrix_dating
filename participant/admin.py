from django.contrib import admin
from participant.models import Client
# --------------------------------------------------------------------------


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'gender')
    list_filter = ('email', 'gender')
    search_fields = ('email', )
