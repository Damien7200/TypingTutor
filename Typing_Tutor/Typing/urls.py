from django.urls import path
from . import views

urlpatterns = [
    #does not get used
    path("", views.home, name="Home"),
    path("wordbank/", views.Wordbank, name="Word_bank"),
    path("practise/", views.Practise, name="Practise")

]