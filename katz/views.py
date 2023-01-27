from django.http import HttpResponse
from django.shortcuts import render


# returns the http request for the main page: http://127.0.0.1:8000/
def index(request):
    return render(request, "../templates/index.html")


# returns the http request for the "available kittens" page: http://127.0.0.1:8000/kittens/
def kittens(request):
    return render(request, "../templates/kittens.html")

# returns the http request for the "register" page: http://127.0.0.1:8000/kittens/
def register(request):
    return render(request, "../templates/register.html")
