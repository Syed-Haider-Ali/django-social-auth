from django.shortcuts import render, redirect
from django.contrib.auth import logout
from rest_framework.viewsets import ModelViewSet

class AuthView(ModelViewSet):
    def home(self,request):
        return render(request, 'auth_app/home.html')

    def logout_user(self,request):
        logout(request)
        return redirect('/')


