# Generated by Django 5.0.2 on 2024-02-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caloriedata',
            name='calories',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]