from django.db import models
from location.models import Location

# Create your models here.

class Parent(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=25,
        verbose_name="Фамилия"
    )
    patronymic = models.CharField(
        max_length=20,
        verbose_name="Отчество"
    )
    phone_number = models.CharField(
        max_length=16,
        verbose_name="Номер телефона"
        )
    passport_serial = models.CharField(
        max_length=4,
        verbose_name="Серия паспорта",
        blank=True,
        null=True
        )
    passport_number = models.CharField(
        max_length=7,
        verbose_name="Номер паспорта",
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Адрес регистрации",
        blank=True,
        null=True
    )

    subscription_price = models.IntegerField(verbose_name="Стоимость абонемента")

    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='parents',
        verbose_name="Локация",
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True, verbose_name="Активный")



    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

    def __str__(self):
        return f"{self.last_name} {self.name} {self.patronymic}"
    
class Child(models.Model):
    child_parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE, 
        related_name='children'
        )
    
    name = models.CharField(
        max_length=20,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=25,
        verbose_name="Фамилия"
    )
    patronymic = models.CharField(
        max_length=20,
        verbose_name="Отчество"
    )
    date_of_birth = models.DateField(verbose_name="Дата рождения")

    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,  # Защищаем от случайного удаления локации
        related_name='students',
        verbose_name="Локация обучения",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.last_name} {self.name}"
    
    class Meta:
        verbose_name = "Ребенок"
        verbose_name_plural = "Дети"


