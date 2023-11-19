from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "map.html")

def restaurant(request):
    item_range = range(1, 5)
    return render(request, "restaurant.html", {"item_range": item_range})

def comments(request):
    comment_range = range(5)
    return render(request, "comments.html", {"comment_range": comment_range})

def compile(request):
    return render(request, "compile.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")