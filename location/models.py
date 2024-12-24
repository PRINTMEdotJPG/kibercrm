from django.db import models

class Location(models.Model):
    """
    Модель локации (места обучения)

    Attributes:
        name: Название локации
        address: Адрес локации
        is_active: Активна ли локация
        created_at: Дата создания записи
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Название локации",
        help_text="Например: Дрожжино, Боброво и т.д."
    )

    address = models.TextField(
        verbose_name="Адрес",
        help_text="Полный адрес локации",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ['name']