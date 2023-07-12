from django.shortcuts import render
from .models import destination

# Create your views here.
dests=destination.objects.all()
def index(request):
    
    return render(request,"index.html",{'dests':dests})
def destinations(request):
        return render(request,"destinations.html",{'dests':dests})