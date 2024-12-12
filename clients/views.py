from django.shortcuts import render, redirect
from .models import Parent, Child
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def view_parents(request):
    if request.user.role in ('MANAGER', 'DIRECTOR'):
        parents = Parent.objects.all()
        return render(request, 'clients/manager_parents_dashboard.html', {
            'parents': parents
            })
    messages.error(request, 'У вас нет доступа к этой странице.')
    return redirect('login')
