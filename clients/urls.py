from django.urls import path
from . import views

urlpatterns = [
    #path('parents/', views.parent_list, name='parent_list'),
    path('manager/locations/', views.manager_locations, name='manager_locations'),
    path('manager/locations/<int:location_id>/parents/', views.location_parents, name='location_parents'),
]

# Надо создать урл функцию, которая будет отображать всех родителей на локации