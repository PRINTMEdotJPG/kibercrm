from django.contrib import admin
from .models import CustomUser, TutorOrAssistant
from .service import generate_password
from django.contrib.auth.hashers import make_password

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    """ Настройка отображения CustomUser в админке """
    list_display = ('username', 'email', 'full_name', 'role', 'get_linked_locations' )
    list_filter = ('role', 'is_staff', 'is_active')

    # Определяем собственные fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('full_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Role & Locations'), {'fields': ('role', 'linked_locations')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fieldsets для создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'full_name', 'email'),
        }),
    )

    search_fields = ('username', 'full_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions', 'linked_locations')

    def get_linked_locations(self, obj):
        return ", ".join([location.name for location in obj.linked_locations.all()])
    get_linked_locations.short_description = 'Закрепленные локации'
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if not obj:  # если создаем нового пользователя
    #         form.base_fields['password'].initial = make_password(generate_password())
    #     return form
    
    def save_model(self, request, obj, form, change):
        if not change:  # Если это создание нового пользователя
            obj.password = make_password(obj.password)
        elif 'password' in form.changed_data:  # Если пароль был изменен
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)


# Register your models here.
