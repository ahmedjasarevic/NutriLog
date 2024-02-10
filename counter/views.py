from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
import requests
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CalorieData
from django.http import HttpResponseBadRequest
from datetime import datetime
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'register':
            return accounts_register(request)
        elif action == 'login':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return JsonResponse({'success': True, 'message': 'Login successful'})
            # If authentication fails, return error message
            return JsonResponse({'success': False, 'message': 'Invalid username or password'}, status=400)
        else:
            query = request.POST.get('query')
            api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
            api_request = requests.get(api_url + query, headers={'X-Api-Key': 'DY7f8vL8tXoVsm1BTazCKw==hePoo35tYXSfHZKK'})
            try:
                api = json.loads(api_request.content)
                print(api)
            except Exception as e:
                api = "There was an error"
                print(api)
            return render(request, 'results.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})



@login_required
def save_calorie_data(request):
    if request.method == 'POST':

        food_name = request.POST.get('food_name')
        current_date = datetime.now().strftime('%Y-%m-%d')
        calories = request.POST.get('calories')
        carbohydrates_total_g = request.POST.get('carbohydrates_total_g')
        cholesterol_mg = request.POST.get('cholesterol_mg')
        fat_saturated_g = request.POST.get('fat_saturated_g')
        fat_total_g = request.POST.get('fat_total_g')
        fiber_g = request.POST.get('fiber_g')
        potassium_mg = request.POST.get('potassium_mg')
        protein_g = request.POST.get('protein_g')
        sodium_mg = request.POST.get('sodium_mg')
        sugar_g = request.POST.get('sugar_g')


        calorie_data = CalorieData.objects.create(
            user=request.user,
            food_name=food_name,
            date=current_date,
            calories=calories,
            carbohydrates_total_g=carbohydrates_total_g,
            cholesterol_mg=cholesterol_mg,
            fat_saturated_g=fat_saturated_g,
            fat_total_g=fat_total_g,
            fiber_g=fiber_g,
            potassium_mg=potassium_mg,
            protein_g=protein_g,
            sodium_mg=sodium_mg,
            sugar_g=sugar_g
        )
        messages.success(request, 'Calorie data saved successfully.')
        return redirect('home')  
    else:
        # Handle invalid request method
        return HttpResponseBadRequest("Invalid request method")
