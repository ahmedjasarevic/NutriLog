from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save-calorie-data/', views.save_calorie_data, name='save_calorie_data'),
]