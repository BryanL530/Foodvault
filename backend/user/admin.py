
from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = (
        'user_name',
        'first_name',
        'last_name',
    )
    list_display = (
        'user_name',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )
    
admin.site.register(User, UserAdmin)