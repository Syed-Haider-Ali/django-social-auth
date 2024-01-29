from django.urls import path
from .views import AuthView

urlpatterns = [
    path('', AuthView.as_view({'get': 'home'})),
    path('logout', AuthView.as_view({'get': 'logout_user'}), name='logout')
]
