
from django.contrib import admin
from django.forms import Textarea

from users.models import NewUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):

    search_fields = ('email', 'user_name', 'first_name')

    list_filter = ('email', 'user_name', 'first_name', 'is_active', )

    ordering = ('-start_date',)
    list_display  = ('email', 'user_name', 'first_name', 'is_active', 'is_staff'
    )
    fieldsets = (
        (None, 
        {'fields': ('email', 'user_name', 'first_name')}),
        ('permissions', {'fields': ('is_staff', 'is_active')}),
        ('personal', {'fields': ('about', )})
    )
    formfields_overrides ={
        NewUser.about : {'widget': Textarea(attrs={'rows': 10, 'cols':40 },)},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )


admin.site.register(NewUser, UserAdminConfig)

# @admin.register(NewUser, UserAdminConfig)
# class ModelUser(admin.ModelAdmin):
#     # list_display = ['user_name', 'email', 'start_date', 'is_staff']

