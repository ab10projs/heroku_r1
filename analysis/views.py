from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def analysis(request):
    return render(request, 'analysis.html', {})

