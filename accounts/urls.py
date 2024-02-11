# accounts/urls.py
from django.urls import path
from . import views

app_name= 'accounts'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.profile_view, name='profile_view'),
]
