from . import views
from django.urls import path
urlpatterns = [
    path("",views.index,name="index"),
    path("/b",views.calculator,name="Retn_calculation")
]
