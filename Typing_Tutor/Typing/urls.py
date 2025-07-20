from django.urls import path
from . import views

urlpatterns = [
  
    path("", views.home, name="Home"),
    path("wordbank/", views.Wordbank, name="Word_bank"),
    # path("practise/", views.Practise, name="Practise"), 
    path("settings/", views.settings, name="settings"),
    path('practise/', views.Practise, name='practise'),
    path('update_word_bank/', views.Update_word_bank, name='update_word_bank'),
    path('Results/', views.Results, name='Results'),
]