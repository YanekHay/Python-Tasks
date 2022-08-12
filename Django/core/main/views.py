from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello Python Team')
# Create your views here.
