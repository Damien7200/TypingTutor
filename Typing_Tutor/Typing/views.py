from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random as r
from django.views.decorators.http import require_http_methods
import json
from django.template.loader import render_to_string




def Practise(request):
    difficulty = request.session['difficulty']
    if difficulty == None:
        difficulty = 'easy'
        request.session['difficulty'] = difficulty
    else:
        difficulty = request.session['difficulty']

    words = get_random_word(request, difficulty)
    words = " ".join(words)
    print(f"{difficulty} session ")
    return render(request, "Typing/practise.html", {'Words' : words, 'difficulty' : difficulty})

def Update_word_bank(request):
    

  
   
    

    if request.method == "POST":
        print("Received AJAX POST")
        data = json.loads(request.body)
        print("Difficulty received:", data)
        difficulty = data.get('difficulty', 'easy')
        words = get_random_word(request, difficulty)  
        words = " ".join(words)
    

    
        html = render_to_string('Typing/partials/wordbank.html', {'word_bank': words})
        return JsonResponse({'html': html, 'words': words})


def Results(request):
    if request.method == "POST":
        data = json.loads(request.body)
        seconds = data.get('seconds')
        minutes = seconds/60
        

        typedOverlay = data.get('typedOverlay')
        
        TText = data.get('TText')
        
        #accuracy measurment
        accuracyCounter = 0
        for i in range(len(typedOverlay)):
           
            if typedOverlay[i] == TText[i]:
                accuracyCounter += 1
           
        accuracyMeasure = (accuracyCounter/len(typedOverlay))*100
       
                
        #raw wpm
        typedOverlay = typedOverlay.strip().split()
        TText = TText.strip().split()
        wpm = round(len(typedOverlay)/minutes,2)

        #valid wpm
        correctWordCount = 0
        for i in range(min(len(TText), len(typedOverlay))):
            if TText[i] == typedOverlay[i]:
                correctWordCount += 1
        validWPM = round(correctWordCount/minutes,2)

        
        

        #run function to compare the typed overlay words with the target words and check ow many are valid. and the calucalate the valid wpm and send this tot ehtemplate with wpm
        html = render_to_string('Typing/partials/results.html', {'wpm' : wpm, 'validWPM' : validWPM, 'accuracyMeasure': int(accuracyMeasure)})
        return JsonResponse({'html': html})
    
def Wordbank(request):
    return render (request, "Typing/Word_bank.html")





def get_random_word(request, difficulty):
        

    programming_terms = {
        "easy": [
            "software", "algorithm", "binary", "debug", "function", "integer",
            "string", "boolean", "output", "input", "loop", "array",
            "variable", "test", "code", "file", "list", "user", "data", "IDE"
        ],
        "medium": [
            "iteration", "selection", "structure", "pseudocode", "refinement",
            "abstraction", "subprogram", "control", "stack", "record", "module",
            "testing", "runtime", "syntax", "logic", "maintenance", "installation",
            "encryption", "validation", "hashing"
        ],
        "hard": [
            "backtracking", "sandboxing", "cryptography", "two_complement",
            "hexadecimal", "authentication", "authorisation", "penetration",
            "vulnerability", "confidentiality", "availability", "race_condition",
            "exception", "session_management", "cross_site_scripting",
            "flowchart", "imperative", "object_oriented", "functional",
            "session", "abnormal", "refactor", "compliance"
        ],
 "PF": [
        "compile",
        "execute",
        "operator",
        "expression",
        "recursion",
        "stack",
        "queue",
        "pointer",
        "algorithm",
        "pseudocode",
        "flowchart",
        "specification",
        "integration",
        "debugging",
        "maintenance",
        "selection",
        "iteration",
        "abstraction",
        "data_structure",
        "twos_complement"
    ],

    "OOP": [
        "abstraction",
        "inheritance",
        "polymorphism",
        "encapsulation",
        "override",
        "attribute",
        "prototype",
        "module",
        "composition",
        "association",
        "generalisation",
        "aggregation",
        "interface",
        "constructor",
        "class_diagram",
        "message_passing",
        "polymorphic_dispatch",
        "method_overloading",
        "facade_pattern",
        "version_control"
    ],

    "PM": [
        "actuation",
        "encoder",
        "servo",
        "calibration",
        "robotics",
        "automation",
        "controller",
        "circuit",
        "analog",
        "digital",
        "microcontroller",
        "sensor_array",
        "actuator",
        "end_effector",
        "degrees_of_freedom",
        "closed_loop",
        "open_loop",
        "firmware",
        "pid_control",
        "power_budget"
    ],

    "SSA": [
        "malware",
        "phishing",
        "token",
        "firewall",
        "cipher",
        "payload",
        "breach",
        "sandbox",
        "checksum",
        "backdoor",
        "data_protection",
        "confidentiality",
        "integrity",
        "availability",
        "authentication",
        "authorisation",
        "accountability",
        "input_validation",
        "sanitisation",
        "session_management"
    ],

    "PFTW": [
        "cookie",
        "session",
        "router",
        "websocket",
        "markup",
        "template",
        "endpoint",
        "backend",
        "frontend",
        "browser",
        "http",
        "https",
        "tcp_ip",
        "dns",
        "ftp",
        "tls",
        "sql",
        "orm",
        "pwa",
        "caching"
    ],

    "SA": [
        "workflow",
        "trigger",
        "pipeline",
        "scheduler",
        "build",
        "deploy",
        "monitor",
        "script",
        "rollback",
        "job",
        "machine_learning",
        "devops",
        "rpa",
        "bpa",
        "supervised_learning",
        "unsupervised_learning",
        "regression_model",
        "neural_network",
        "decision_tree",
        "reinforcement_learning"
    ]
    }
 
    WBwords = programming_terms[difficulty]
    r.shuffle(WBwords)
    request.session['Word_Amount'] = len(WBwords)
   
    return (programming_terms[difficulty])

    


