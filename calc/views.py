from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html',{'name':"Benjamin Koshy Biju",'quote':'I will succeed'})
# def calculator(request):
#     return HttpResponse(5+6)

