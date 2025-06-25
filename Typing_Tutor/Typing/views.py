from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "Typing/home.html")

def Practise(request):
    words = "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    if request.method == "POST":
        pass
    

    return render(request, "Typing/practise.html", {'Words' : words} )

def Wordbank(request):
    return render (request, "Typing/Word_bank.html")




