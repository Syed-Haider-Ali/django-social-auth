from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('logout', logout_user, name='logout')
]
