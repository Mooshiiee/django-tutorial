from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s. % question_id")