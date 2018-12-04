from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_movie(request):
    # print(request.POST)

    # https://itunes.apple.com/search?term=beyonce&entity=musicVideo
    url = "https://itunes.apple.com/search?term="
    url += request.POST['user_input']
    url += "&entity=musicVideo"

    print(url)

    # print(url)
    r = requests.get(url)
    # print(r.content)

    return HttpResponse(r.content, content_type='application/json')
