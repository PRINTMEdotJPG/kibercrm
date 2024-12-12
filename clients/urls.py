from django.urls import path
from .views import view_parents

urlpatterns = [
    path('parents/', view_parents, name='view_parents')
]

# Надо создать урл функцию, которая будет отображать всех родителей на локации