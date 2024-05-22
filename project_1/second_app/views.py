from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def machine(request):
    return HttpResponse("I love machine learning")

def data(request):
    return HttpResponse("I love data")
