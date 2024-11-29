from django.contrib import admin
from .models import CustomUser, TutorOrAssistant
from .service import generate_password

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # если создаем нового пользователя
            form.base_fields['password'].initial = generate_password()
        return form


# Register your models here.
