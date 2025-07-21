from django.shortcuts import render
from django.http import *

def index_view(request):
    return HttpResponse("<h1>Home page</h1>")

def Contact_view(request):
    return HttpResponse("<h1>Contact page</h1>")
