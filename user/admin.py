from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models in admin panels here.

from .models import CustomUser

# declaring Customuser admin panel


class CustomUserAdmin(UserAdmin):

    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

# calling in admin panel


admin.site.register(CustomUser, CustomUserAdmin)
