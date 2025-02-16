# forms.py
from django import forms
from django.contrib.auth import get_user_model
from .models import Parent, Child
from datetime import date

User = get_user_model()

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = [
            'last_name', 'name', 'patronymic', 
            'phone_number', 'location', 'subscription_price'
        ]

    def __init__(self, *args, **kwargs):
        # Получаем пользователя из аргументов формы
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Фильтруем локации только те, что доступны менеджеру
        if self.user and self.user.is_manager:
            self.fields['location'].queryset = self.user.linked_locations.all()


class ChildForm(forms.ModelForm):
    """Форма для создания/редактирования ребенка"""
    class Meta:
        model = Child
        fields = ['name', 'last_name', 'patronymic', 'date_of_birth', 'location']

    def __init__(self, *args, **kwargs):
        # Явно извлекаем parent_id из kwargs формы
        self.parent_id = kwargs.pop('parent_id', None)  # Исправление здесь
        super().__init__(*args, **kwargs)

        # Настройка полей
        self.fields['date_of_birth'].widget = forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )
        self.fields['location'].widget.attrs.update({'class': 'form-select'})
        self.fields['patronymic'].required = False

    def clean_date_of_birth(self):
        """Валидация даты рождения"""
        date_of_birth = self.cleaned_data.get('date_of_birth')
        # Проверяем что возраст не менее 3 лет
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 3:
                raise forms.ValidationError("Ребенок должен быть старше 3 лет")
        return date_of_birth
