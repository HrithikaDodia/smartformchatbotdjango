from django.shortcuts import render

# Create your views here.
dictm = {}
dictcont = ['what is your firstname', 'what is your last name']
dictmap = ['firstname', 'lastname']

def index(request):
    return render(request, 'chatbotapp/index.html', {})

def send_response_chatbot(msg, scope):
    a = scope["session"]["seed"]
    val = dictcont[a]
    if a>0:    
        key = dictmap[a-1]
        dictm[key] = msg
    scope["session"]["seed"] += 1
    return val 

def show(request):
    return render(request, 'chatbotapp/show.html', {"a": dictm})