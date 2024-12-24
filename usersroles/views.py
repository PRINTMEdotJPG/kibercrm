from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Редирект в зависимости от роли
                if user.role == 'DIRECTOR':
                    return redirect('admin_dashboard')
                elif user.role == 'MANAGER':
                    return redirect('manager_dashboard')
                #elif user.role == 'manager':
                 #   return redirect('manager_dashboard')
                #else:
                #    return redirect('tora_dashboard')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = LoginForm()

    return render(request, 'usersroles/login.html', {
        'form': form
        })

def logout_view(request):
    logout(request)
    return redirect('login')

def admin_dashboard(request):
    users = CustomUser.objects.all()
    return render(request, 'usersroles/admin_dashboard.html', {
        'users': users
        })

def manager_dashboard(request):
    users = CustomUser.objects.all()
    return render(request, 'usersroles/manager_dashboard.html', {
        'users': users
        })