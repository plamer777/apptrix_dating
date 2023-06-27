from django.contrib import admin
from core.models import User
# --------------------------------------------------------------------------


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email', 'is_active')
    search_fields = ('username', 'email')
