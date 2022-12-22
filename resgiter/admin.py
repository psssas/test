from django.contrib import admin

from .models import Account

# Register your models here.

class AccoumtAdmin(admin.ModelAdmin):
    list_display = ("name", "password")

admin.site.register(Account, AccoumtAdmin)