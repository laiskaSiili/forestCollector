from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StandInformation, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class StandInformationAdmin(admin.ModelAdmin):
    pass

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_editable = ['username', 'email', 'is_collector']
    list_display = ['username', 'email', 'is_collector']
    list_display_links = None
    list_filter = []
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'is_collector')
        }),
    )

admin.site.register(StandInformation, StandInformationAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
