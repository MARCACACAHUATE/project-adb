from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.forms import UserCreationForm, UserChangeForm
from usuarios.models import Usuarios


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Usuarios
    list_display = ("matricula", "is_staff", "is_active",)
    list_filter = ("matricula", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("matricula", "password",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "matricula", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("matricula",)
    ordering = ("matricula",)


admin.site.register(Usuarios, CustomUserAdmin)
