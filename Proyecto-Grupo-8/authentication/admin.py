from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'profile_type', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('profile_type', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name', 'last_name')
    ordering = ('id',)

@admin.register(models.ProfileType)
class ProfileTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type','name')
    search_fields = ('name',)
    ordering = ('id',)