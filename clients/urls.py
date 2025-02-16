from django.urls import path
from . import views

urlpatterns = [
    #path('parents/', views.parent_list, name='parent_list'),
    path('manager/locations/', views.manager_locations, name='manager_locations'),
    path('manager/locations/<int:location_id>/parents/', views.location_parents, name='location_parents'),
     path('parents/create/', views.ParentCreateView.as_view(), name='parent_create'),
    path(
        'parents/<int:parent_id>/children/create/', 
        views.ChildCreateView.as_view(), 
        name='child_create'
    ),
    path('parents/', views.ParentListView.as_view(), name='parent_list'),
]


# urlpatterns = [
    #path('parents/', ParentListView.as_view(), name='parent_list'),
   
# ]


