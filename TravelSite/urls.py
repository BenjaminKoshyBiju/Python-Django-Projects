from .import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='home'),
    path('destinations',views.destinations,name="destinations")
]
