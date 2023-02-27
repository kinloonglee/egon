from django.contrib import admin

# Register your models here.
from api import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

class UserAdmin(DjangoUserAdmin):
    # 添加用户课操作字段
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'mobile', 'groups', 'user_permissions'),
        }),
    )
    # 展示用户呈现的字段
    list_display = ('username', 'mobile', 'is_staff', 'is_active', 'is_superuser')

admin.site.register(models.User)
admin.site.register(models.Car)
admin.site.register(models.Book)
