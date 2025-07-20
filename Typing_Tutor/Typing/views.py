from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random as r
from django.views.decorators.http import require_http_methods
import json
from django.template.loader import render_to_string


def home(request):
    return render(request, "Typing/home.html")

def Practise(request):
   
    difficulty = request.session['difficulty']
    if difficulty == None:
        request.session['difficulty'] = 'easy'
        
    else:
        difficulty = request.session['difficulty']
    words = get_random_word(difficulty)
    words = " ".join(words)
    print(f"{difficulty} session ")
    return render(request, "Typing/practise.html", {'Words' : words, 'difficulty' : difficulty})

def Update_word_bank(request):
    

  
   
    
    if request.method == "POST":
        print("Received AJAX POST")
        data = json.loads(request.body)
        print("Difficulty received:", data)
        difficulty = data.get('difficulty', 'easy')
        words = get_random_word(difficulty)  
        words = " ".join(words)
    

    
        html = render_to_string('Typing/partials/wordbank.html', {'word_bank': words})
        return JsonResponse({'html': html, 'words': words})


def Results(request):
    if request.method == "POST":
        data = json.loads(request.body)
        wpm = data.get('wpm')
        html = render_to_string('Typing/partials/results.html', {'wpm' : wpm})
        return JsonResponse({'html': html})
    
def Wordbank(request):
    return render (request, "Typing/Word_bank.html")

def settings(request):
    #get the difficulty fromt he drop down
    difficulty = request.POST.get('difficulty')
    request.session['difficulty'] = difficulty

    return render(request, "Typing/settings.html")

def get_random_word(difficulty):
        

    basic_terms = [
    "software", "algorithm", "binary", "debug", "function", "integer",
    "string", "boolean", "output", "input", "loop", "array",
    "variable", "test", "code", "file", "list", "user", "data", "IDE"
]

    medium_terms = [
    "iteration", "selection", "structure", "pseudocode", "refinement",
    "abstraction", "subprogram", "control", "stack", "record", "module",
    "testing", "runtime", "syntax", "logic", "maintenance", "installation",
    "encryption", "validation", "hashing"
]

    difficult_terms = [
    "backtracking", "sandboxing", "cryptography", "two_complement",
    "hexadecimal", "authentication", "authorisation", "penetration",
    "vulnerability", "confidentiality", "availability", "race_condition",
    "exception", "session_management", "cross_site_scripting",
    "flowchart", "imperative", "object_oriented", "functional",
    "session", "abnormal", "refactor", "compliance"
]
    if difficulty == "easy":
        r.shuffle(basic_terms)
        return basic_terms
    elif difficulty == "medium":
        r.shuffle(medium_terms)
        return medium_terms
    elif difficulty == "hard":
        r.shuffle(difficult_terms)
        return difficult_terms
    else:
        return []


