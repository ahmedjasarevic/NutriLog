from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
import requests
import json
from django.shortcuts import render, redirect

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
