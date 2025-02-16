# views.py

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Parent, Child
from usersroles.models import CustomUser
from location.models import Location
from django.db.models import Count, Q, FilteredRelation
from django.core.exceptions import PermissionDenied

from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import ParentForm, ChildForm

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



class ManagerRequiredMixin(UserPassesTestMixin):
    """Миксин для проверки прав менеджера"""
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manager

class ParentCreateView(ManagerRequiredMixin, CreateView):
    model = Parent
    form_class = ParentForm
    template_name = 'clients/crm/parent_create.html'
    success_url = reverse_lazy('parent_list')

    def get_form_kwargs(self):
        """Передаем пользователя в форму"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """Автоматическое сохранение связанной локации"""
        form.instance.location = form.cleaned_data['location']
        return super().form_valid(form)

class ParentListView(ManagerRequiredMixin, ListView):
    model = Parent
    template_name = 'clients/manager_parents_dashboard.html'

    def get_queryset(self):
        """Фильтрация родителей по локациям менеджера"""
        return Parent.objects.filter(
            location__in=self.request.user.linked_locations.all()
        )

class ChildCreateView(CreateView):
    """View для создания ребенка"""
    model = Child
    form_class = ChildForm
    template_name = 'clients/crm/child_create.html'

    def get_form_kwargs(self):
        """Добавляем parent_id в kwargs формы явно"""
        kwargs = super().get_form_kwargs()
        kwargs['parent_id'] = self.kwargs.get('parent_id')
        return kwargs

    def form_valid(self, form):
        """Привязка к родителю должна быть через правильное поле"""
        form.instance.child_parent = Parent.objects.get(pk=self.kwargs['parent_id'])  # Используем child_parent

        if not form.instance.location:
            parent = form.instance.child_parent
            form.instance.location = parent.location

        return super().form_valid(form)

    def get_success_url(self):
        """Редирект после успешного создания"""
        try:
            parent_id = self.kwargs['parent_id']
            parent = Parent.objects.get(id=parent_id)  # Получаем объект Parent
            if parent.location:
                return reverse('location_parents', kwargs={'location_id': parent.location.id})
        except Parent.DoesNotExist:
        # Обработка случая, если родитель не найден
            pass
        except AttributeError:
        # Обработка случая, если у родителя нет локации
            pass

        # Возвращаем дефолтный URL, если что-то пошло не так
        return reverse('manager_locations')

