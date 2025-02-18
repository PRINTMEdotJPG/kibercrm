from django.db import models
from django.utils import timezone
from location.models import Location
from clients.models import Child

class Group(models.Model):
    """
    Модель учебных групп с расписанием и статусами
    Attributes:
        name (str): Название группы (max 100 символов)
        location (Location): Привязка к локации (ForeignKey)
        students (Student): Ученики группы (ManyToMany)
        schedule (str): Расписание занятий в текстовом формате
        start_date (date): Дата начала работы группы
        status (str): Статус группы (active/archive)
    """
    STATUS_CHOICES = [
        ('active', 'Активная'),
        ('archive', 'Архивная'),
    ]

    name = models.CharField('Название группы', max_length=100)
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        verbose_name='Локация',
        related_name='groups',
        help_text='Выберите локацию из списка'
    )
    students = models.ManyToManyField(
        Child,
        verbose_name='Ученики',
        related_name='groups',
        blank=True,
        help_text='Выберите учеников для этой группы'
    )
    schedule = models.TextField(
        'Расписание',
        help_text='Пример: Пн/Ср/Пт 18:00-20:00'
    )
    start_date = models.DateField(
        'Дата начала',
        default=timezone.now,
        help_text='Дата первого занятия группы'
    )
    status = models.CharField(
        'Статус группы',
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        help_text='Активные группы отображаются в общем списке'
    )

    def __str__(self):
        """Отображение группы в формате: ИмяГруппы (Локация)"""
        return f"{self.name} ({self.location})"
    
    def get_students_list(self):
        return ", ".join([child.full_name for child in self.students.all()])
    get_students_list.short_description = 'Список учеников'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        indexes = [
            models.Index(fields=['status', 'start_date']),
        ]
