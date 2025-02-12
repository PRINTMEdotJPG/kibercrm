# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Parent
from usersroles.models import CustomUser
from location.models import Location
from django.db.models import Count, Q, FilteredRelation
from django.core.exceptions import PermissionDenied

from django.db.models import Count, Q

@login_required
def manager_locations(request):
    user = request.user
    locations = user.linked_locations.annotate(
        num_active_students=Count(
            'students',  # related_name от Child к Location
            filter=Q(students__child_parent__is_active=True)
        )
    )
    context = {'locations': locations}
    return render(request, 'clients/active_locations_for_manager.html', context)


@login_required
def location_parents(request, location_id):
    user = request.user
    if user.role not in ("MANAGER", "DIRECTOR"):
        return redirect('/login')
    location = get_object_or_404(Location, id=location_id)

    if user.role == CustomUser.Roles.DIRECTOR:
        # Директор видит всех родителей в локации
        parents = Parent.objects.filter(location=location)
    elif user.role == CustomUser.Roles.MANAGER:
        if location in user.linked_locations.all():
            # Менеджер видит родителей только из своих локаций
            parents = Parent.objects.filter(location=location)
        else:
            # Если локация не принадлежит менеджеру, доступ запрещен
            
            raise PermissionDenied

    context = {
        'parents': parents,
        'location': location
    }
    return render(request, 'clients/manager_parents_dashboard.html', context)

