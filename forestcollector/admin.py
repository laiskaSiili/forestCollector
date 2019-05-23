from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StandInformation, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class StandInformationAdmin(admin.ModelAdmin):
    list_display = ['creator', 'created_at']

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_editable = ['is_collector']
    list_display_links = ['username']
    list_display = ['username', 'email', 'is_collector']
    list_filter = []
    fieldsets = (
        ('None', {
            'fields': ('username', 'password', 'email', 'is_collector')
        }),
    )

admin.site.register(StandInformation, StandInformationAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
