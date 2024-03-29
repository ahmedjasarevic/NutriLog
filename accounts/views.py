from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


from django.utils import timezone
from counter.models import CalorieData
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username, email=email, password=password)
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('/')  # Redirect to the home page
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Login successful'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid username or password'}, status=400)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'message': errors}, status=400)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

from django.utils import timezone

def profile_view(request):
    user_id = request.user.id
    current_date = timezone.now().date()

    calorie_data = CalorieData.objects.filter(user_id=user_id, date=current_date)
    total_protein = sum(data.protein_g for data in calorie_data)
    total_calories = sum(data.calories for data in calorie_data)
    total_sugar = sum(data.sugar_g for data in calorie_data)
    
    context = {
        'calorie_data': calorie_data,
        'total_protein': total_protein,
        'total_calories': total_calories,
        'total_sugar': total_sugar
    }
    return render(request, 'profile.html', context)
