from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from carts.models import Cart

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{user.first_name}, Вы вошли в аккаунт")
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserLoginForm()
        
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{request.user.first_name}, Вы успешно зарегистрировались")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{request.user.first_name}, Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        "form": form
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.first_name}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))