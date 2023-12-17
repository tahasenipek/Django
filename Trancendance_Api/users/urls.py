from django.urls import path
from .views import register_user, get_users

urlpatterns = [
    path('register', register_user),
    path('getUser', get_users)
]
