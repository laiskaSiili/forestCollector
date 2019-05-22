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
    list_display = ['email', 'username', 'is_collector']

admin.site.register(StandInformation, StandInformationAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
