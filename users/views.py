from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models, forms

#регистрация

def register_view(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomUserCreationForm()
    return render(request, template_name='users/register.html', 
                  context={'form': form})


#авторизация
def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:user_list')
    else:
        form = AuthenticationForm()
    return render(request, template_name='users/login.html', 
                  context={'form':form})

#Выход из сессии(из личного кабинета)
def auth_logout_view(request):
    logout(request)
    return redirect('users:login')



#UserList
def user_list_view(request):
    if request.method == 'GET':
        users = User.objects.all().order_by('-id')
        #users = models.CustomUser.objects.all().order_by('-id')
    return render(request, template_name='users/user_list.html',
                  context={
                      'users': users
                  })