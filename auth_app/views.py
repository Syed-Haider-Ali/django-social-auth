from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'auth_app/home.html')

def logout_user(request):
    logout(request)
    return redirect('/')


