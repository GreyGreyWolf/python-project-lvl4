from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email"]
    list_filter = ['lastname']
    search_fields = ['firstname', 'lastname', 'email']

        
        
    class Meta:
        model = User


admin.site.register(User, UserAdmin)