from django.contrib import admin
from .models import CustomUser, TutorOrAssistant
from .service import generate_password
from django.contrib.auth.hashers import make_password

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role')

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
