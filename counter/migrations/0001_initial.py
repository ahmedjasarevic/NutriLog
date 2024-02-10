# Generated by Django 5.0.2 on 2024-02-10 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CalorieData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('carbohydrates_total_g', models.FloatField()),
                ('cholesterol_mg', models.FloatField()),
                ('fat_saturated_g', models.FloatField()),
                ('fat_total_g', models.FloatField()),
                ('fiber_g', models.FloatField()),
                ('potassium_mg', models.FloatField()),
                ('protein_g', models.FloatField()),
                ('sodium_mg', models.FloatField()),
                ('sugar_g', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]