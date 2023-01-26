from django.urls import path

# Import all methods from views.py
from . import views

# This is a list of the URL path names (webpages) and their corresponding "view" name.
# The view name is the name of the matching method from the views.py file.
urlpatterns = [
    path('', views.index, name='index'),
    path('kittens/', views.kittens, name='kittens'),



]