from django.contrib import admin
from .models import CalorieData

@admin.register(CalorieData)
class CalorieDataAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'date', 'calories', 'user')
    list_filter = ('date', 'user')
