from django.http import HttpResponse


# returns the http request for the main page: www.
def index(request):
    return HttpResponse("Hello, world. You're at the katz index (main webpage).")


# returns the http request for the "available kittens" page: www.
def kittens(request):
    return HttpResponse("This is the page where the available kittens will go.")
