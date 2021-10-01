from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.forms import Textarea

class UserAdminConfig(UserAdmin):
    """
    CUSTOM ADMIN INTERFACE
    ORDER ITEMS BY RECENT START DATE
    AND SHOWS EMAIL, USERNAME AND STATUS
    """
    model = User
    search_fields = ('email', 'username')
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'is_active', 'is_staff')
    
    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')},),
        ('Personnal', {'fields': ('about',)})
        )
    
    formfield_overrides = {
        User.about: {'widget': Textarea(attrs={'rows':10, 'cols':40})}
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(User, UserAdminConfig)