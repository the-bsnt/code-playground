from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ("username", "email", "address", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("address",)}),)
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("address",)}),);

    # ⚠️ The Mistake That Causes the Error
    # If you copy Django's internal admin (UserAdmin.add_fieldsets) form structure or use a third-party package, it may try to include a non-existent field like "usable_password" in add_fieldsets.
    # so Do NOT include "usable_password" in fields or add_fieldsets. just use this
    add_fieldsets = (
        (
            "Add User",
            {"fields": ("username", "email", "address", "password1", "password2")},
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
