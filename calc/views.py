from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'indexx.html',{'name':"Benjamin Koshy Biju",'quote':'I will succeed'})
def result(request):
    num1=int(request.POST['n1'])
    num2=int(request.POST['n2'])
    n3=num1+num2
    return render(request,'result.html',{'res':n3})

