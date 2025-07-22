from django.shortcuts import render
from django.http import *

def index_view(request):
    return render(request, 'index.html')

def Contact_view(request):
    return render(request, 'contact.html')

def About_view(request):
    return render(request, 'about.html')
