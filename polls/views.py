from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello my views code is working!!! This is probably the Index page.")
def page2(request):
    return HttpResponse("This is 2nd page sub of Index page ")
