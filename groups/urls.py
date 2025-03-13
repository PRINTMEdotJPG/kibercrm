from django.urls import path
from . import views
urlpatterns = [
    path(
        'groups/',
        views.GroupListView.as_view(),
        name='group_list_all'
    ),
    path(
        'locations/<int:location_id>/groups/',
        views.LocationGroupListView.as_view(),
        name='group_list_by_location'
    ),
    path('groups/<int:pk>/',
          views.group_detail,
        name='group_detail'),

    # path('locations/group_detail/<int:group_id>',
    #      views.GroupDetailView.as_view(),
    #      name='group_detail')
    # path(
    #     'groups/<int:pk>/',
    #     views.GroupDetailView.as_view(),
    #     name='group_detail'
    # ),
]
"""
URL-конфигурация для модуля групп

Структура:
1. Просмотр всех групп:
    URL: /groups/
    Имя маршрута: 'group_list_all'
    View: GroupListView

2. Фильтр групп по локации:
    URL: /locations/<ID локации>/groups/
    Имя маршрута: 'group_list_by_location'
    View: LocationGroupListView
    Параметры:
        location_id (int): ID локации в базе данных

3. Детальный просмотр группы:
    URL: /groups/<ID группы>/
    Имя маршрута: 'group_detail'
    View: GroupDetailView
    Параметры:
        pk (int): ID группы

Примеры использования:
- Все группы: reverse('groups:group_list_all')
- Группы локации 5: reverse('groups:group_list_by_location', kwargs={'location_id': 5})
- Группа 12: reverse('groups:group_detail', kwargs={'pk': 12})
"""