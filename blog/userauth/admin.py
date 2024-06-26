from django.contrib import admin
from .models import User, Group


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at']


admin.site.register(User, UserAdmin)