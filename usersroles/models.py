from django.contrib.auth.models import AbstractUser
from django.db import models
from location.models import Location

class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        DIRECTOR = 'DIRECTOR', 'Директор'
        MANAGER = 'MANAGER', 'Менеджер'
        TUTOR = 'TUTOR', 'Тьютор'
        ASSISTANT = 'ASSISTANT', 'Ассистент'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.ASSISTANT
    )

    full_name = models.CharField(
        max_length=100,
        verbose_name="ФИО",
        blank=True
    )
    linked_locations = models.ManyToManyField(
        Location,
        related_name="staff",
        verbose_name="Закрепленные локации для работы",
        )


    # Методы проверки ролей
    def is_director(self):
        return self.role == self.Roles.DIRECTOR

    def is_manager(self):
        return self.role == self.Roles.MANAGER

    def is_tutor(self):
        return self.role == self.Roles.TUTOR

    def is_assistant(self):
        return self.role == self.Roles.ASSISTANT

    # Метод для проверки доступа к функционалу тьютора
    def has_tutor_access(self):
        return self.role in [self.Roles.TUTOR, self.Roles.ASSISTANT]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class TutorOrAssistant(models.Model):
    user = models.ForeignKey(CustomUser, related_name="TorA", on_delete=models.CASCADE)
    salary_in_hour = models.IntegerField(verbose_name="Ставка в час")
    work_hours_in_month = models.IntegerField(
        default=0,
        verbose_name="Количество отработанных часов в этом месяце")
    salary_in_month = models.IntegerField(
        default=0,
        verbose_name="Итоговая зарплата за месяц")
    
    def _calculate_salary(self):
        self.salary_in_month = self.salary_in_hour * self.work_hours_in_month
    

    
    
