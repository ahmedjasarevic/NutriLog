from django.db import models
from django.contrib.auth.models import User

class CalorieData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    date = models.DateField()
    calories = models.FloatField()
    carbohydrates_total_g = models.FloatField()
    cholesterol_mg = models.FloatField()
    fat_saturated_g = models.FloatField()
    fat_total_g = models.FloatField()
    fiber_g = models.FloatField()
    potassium_mg = models.FloatField()
    protein_g = models.FloatField()
    sodium_mg = models.FloatField()
    sugar_g = models.FloatField()

    def __str__(self):
        return self.food_name
