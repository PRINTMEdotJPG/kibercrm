# admin.py
from django.contrib import admin
from .models import Group
from django.utils.html import format_html

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    Админ-панель для управления группами
    С фильтрами по локациям и статусам групп
    """
    list_display = ('name', 'location', 'start_date', 'status', 'students_count')
    list_filter = ('location', 'status')
    filter_horizontal = ('students',)
    search_fields = ('name', 'location__name')

    def status_badge(self, obj):
        """Отображение статуса в виде цветного бейджа"""
        color = 'green' if obj.status == 'active' else 'grey'
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            obj.get_status_display()
        )
    
    def students_count(self, obj):
        return obj.students.count()
    students_count.short_description = 'Учеников'

    status_badge.short_description = 'Статус'
