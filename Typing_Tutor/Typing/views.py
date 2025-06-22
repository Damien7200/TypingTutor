from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "Typing/home.html")

def Practise(request):
    return render(request, "Typing/practise.html")

def Wordbank(request):
    return render (request, "Typing/Word_bank.html")