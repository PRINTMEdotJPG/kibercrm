from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    search_fields = ('name', 'address')

    def get_staff_count(self, obj):
        return obj.staff.count()
    get_staff_count.short_description = 'Кол-во сотрудников'
