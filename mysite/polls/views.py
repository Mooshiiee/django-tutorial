from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse("Hello index of polls/")
    
def moosie(request):
    return HttpResponse("<h1>Moosies Page</h1> <p>fuck i love routing<p>")
    
def detail(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)
#join() takes all items in an iterable and joins them into one string, must have a seperator

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s. % question_id")
    
def what():
    return 1
