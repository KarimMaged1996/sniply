from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, customUserCreationForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = customUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("profile_image",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("profile_image",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
