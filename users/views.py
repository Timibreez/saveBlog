from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from . import forms
from users.forms import LoginForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('saveNow:index')
    else:
        form = SignUpForm()
    return render(request,'users/signup.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('saveNow:index')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('saveNow:index')