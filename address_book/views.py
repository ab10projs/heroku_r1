from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("home HttpResponse")

def add_address(request):
    return render(request, 'add_address.html', {})
