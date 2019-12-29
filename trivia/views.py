from django.views.generic import DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from trivia.models import Question, Choice

def index(request):
    """View function for home page of TRIVIA."""
    template_name = 'trivia/game.html'

    # Generate counts of some of the main objects
    num_questions = Question.objects.all().count()

    context = {
        'num_questions': num_questions,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template_name, context=context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
