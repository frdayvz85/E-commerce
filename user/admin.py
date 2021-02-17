from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'city', 'country','image_tag']
    search_fields = ['user_name']
    readonly_fields = ['image_tag']
admin.site.register(UserProfile, UserProfileAdmin)