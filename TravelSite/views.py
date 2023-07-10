from django.shortcuts import render
from .models import destination
dest1=destination()
dest1.name="Goa"
dest1.price=800
dest1.img='destination_1.jpg'
dest1.desc="We got the Goods"
dest1.offer=True
dest2=destination()
dest2.name='Kerala'
dest2.img='destination_2.jpg'
dest2.price=400
dest2.desc='Gods own country'
dest2.offer=False
dest3=destination()
dest3.name='Somewhere in America'
dest3.img='destination_3.jpg'
dest3.desc='American Tour'
dest3.price=1000
dest3.offer=True
# Create your views here.
def index(request):
    dests=[dest3,dest1,dest2]
    return render(request,"index.html",{'dests':dests})