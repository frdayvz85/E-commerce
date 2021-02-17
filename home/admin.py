from django.contrib import admin
from home.models import Setting, ContactFormMessage, FAQ

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','update_at']

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','subject','message','create_at', 'status']
    list_filter = ['status']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['orderrnumber', 'question','create_at', 'status']
    list_filter = ['status']


admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(FAQ, FAQAdmin)