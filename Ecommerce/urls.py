from .import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    #path('destinations',views.destinations,name="destinations")
]