from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
        return HttpResponse("Hello index of polls/")
    
def moosie(request):
        return HttpResponse("<h1>Moosies Page</h1> <p>fuck i love routing<p>")
