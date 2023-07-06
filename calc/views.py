from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is index of calc")
def calculator(request):
    return HttpResponse(5+6)

