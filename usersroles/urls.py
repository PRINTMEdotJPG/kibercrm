from django.urls import path
from .views import login_view, logout_view, admin_dashboard, manager_dashboard
#manager_dashboard, tora_dashboard

urlpatterns = (
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/admin', admin_dashboard, name='admin_dashboard'),
    path('manager/dashboard/', manager_dashboard, name='manager_dashboard'),
    #path('tora/dashboard/', tora_dashboard, name='tora_dashboard'),
)
