from django.contrib import admin
from .models import User, Sponsor, Profile
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'course', 'account_number')
    search_fields = ('user__email', 'phone', 'course__name', 'account_number')
    list_filter = ('course',)
    
    

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'recommended_by')
    search_fields = ('user__email', 'phone', 'course__name', 'recommended_by__email')
    list_filter = ('user__email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Profile, ProfileAdmin)
