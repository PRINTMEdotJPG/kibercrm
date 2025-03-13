# views.py
from django.views.generic import ListView, DetailView
from .models import Group
from location.models import Location
from django.shortcuts import get_object_or_404, render

class LocationGroupListView(ListView):
    model = Group
    template_name = 'groups/location_groups.html'
    context_object_name = 'groups'
    paginate_by = 15  # Оптимальное количество групп на странице

    def get_queryset(self):
        # Фильтрация по конкретной локации и активным группам
        location_id = self.kwargs['location_id']
        return (
            Group.objects
            .filter(location__id=location_id, status='active')
            .select_related('location')
            .prefetch_related('students')
            .order_by('-start_date')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location_id = self.kwargs['location_id']
        context['current_location'] = get_object_or_404(Location, pk=location_id)
        return context

class GroupListView(LocationGroupListView):
    """
    Отображает все активные группы без привязки к локации.

    Переопределяет:
        get_queryset: Убирает фильтр по локации
        get_context_data: Не передает текущую локацию
    """
    def get_queryset(self):
        """
        Возвращает все активные группы.

        Фильтры:
            - status: Только активные группы ('active')

        Оптимизации:
            То же, что и у LocationGroupListView
        """
        return (
            Group.objects
            .filter(status='active')
            .select_related('location')
            .prefetch_related('students')
            .order_by('-start_date')
        )

    def get_context_data(self, **kwargs):
        """
        Убираем параметры связанные с конкретной локацией.
        """
        context = super().get_context_data(**kwargs)
        context.pop('current_location', None)
        return context
    
def group_detail(request, pk):
    """
    Представление выводит детальную информацию о группе и её учениках.

    Args:
        request (HttpRequest): объект запроса пользователя
        pk (int): первичный ключ объекта группы (Group), получаемый из URL

    Returns:
        HttpResponse: отрендеренный шаблон с деталями группы
    """
    # Получаем объект группы по первичному ключу (pk),
    # либо выдаём страницу 404, если такой группы не существует
    group = get_object_or_404(Group, pk=pk)

    # Передаем объект группы в шаблон
    context = {
        'group': group,
        'students': group.students.all(),  # queryset учеников группы
    }

    return render(request, 'groups/group_detail.html', context)