from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


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
    question = get_object_or_404(Question, pk=question_id)
    try:
        print("vote: try method has ran")
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) #access the post request
    except (KeyError, Choice.DoesNotExist):             
        #redisplay vote form with error message
        print("vote: except has rn")
        return (request, "polls/detail.html",
            {
            "question": question,
            "error_message": "you didnt select a choice."
            },
        )
    else:
        print("vote: else has ran")
        selected_choice.votes += 1
        selected_choice.save()
        print("vote: save has ran")
        return HttpResponseRedirect(reverse("polls:results", args=(question.id))) #using reverse() to get around hardcoding the URL
        #alwasy return HttpResponseRedirect after dealing with post data to prevent double submission,
        #in this case we redirect to the results page\

def moosie(request):
    return render(request, "polls/moosie.html")