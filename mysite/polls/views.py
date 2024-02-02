from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    #context dictionary is used to confirm variable/class names between template
    #and renderer. 
    
    
def moosie(request):
    return HttpResponse("<h1>Moosies Page</h1> <p>fuck i love routing<p>")
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s. % question_id")