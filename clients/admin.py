from django.contrib import admin
from .models import Parent, Child
from location.models import Location

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'patronymic', 'phone_number', 'location')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'patronymic', 'location')

