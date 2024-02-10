from django.shortcuts import render
import requests
import json

def home(request):
    if request.method == 'POST':
        query = request.POST.get('query')  # Use .get() to safely retrieve the query
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
