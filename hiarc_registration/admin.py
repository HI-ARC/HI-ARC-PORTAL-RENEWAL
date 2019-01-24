from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .forms import HiarcUserCreationForm1, HiarcUserCreationForm2, HiarcUserCreationForm3
from .models import HiarcUser

class HiarcUserResource(resources.ModelResource):
    class Meta:
        model = HiarcUser
        fields = ('email', 'username', 'real_name', 'first_name' 'status', 'last_name', 'phone_number', 'motivation', 'portfolio', 'is_staff', 'is_active', )

# Register your models here.
class HiarcUserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = HiarcUserResource
    # form = [HiarcUserCreationForm1, HiarcUserCreationForm2, HiarcUserCreationForm3]
    list_display = ("email", "real_name", "first_name", "last_name", "status", "phone_number", "motivation", "portfolio", "is_staff", "is_active")
    list_filter = ["is_staff", "is_active"]

    fieldsets =  (
        (None, {
            'classes': ('wide',),
            'fields': ("email", "username", "real_name", "status", "phone_number", "motivation", "portfolio", "groups", "is_active", "is_staff", "password1", "password2")
        }),
    )

admin.site.register(HiarcUser, HiarcUserAdmin)
