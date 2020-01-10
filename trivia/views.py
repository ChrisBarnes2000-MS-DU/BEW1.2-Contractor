from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from trivia.models import Question, Choice
from locations.models import Page
from django.urls import reverse
from django.views import generic
import requests
import json

def trivia(request, slug):
    """View function for home page of TRIVIA."""
    template_name = 'trivia/game.html'

    # Generate counts of some of the main objects
    # questions = Question.objects.filter(quiz__slug=slug)
    questions = Question.objects.filter(quiz__slug=slug)
    choices = Choice.objects.filter(question__quiz__slug=slug).order_by('created')
    num_questions = questions.count()

    total_points = sum([question.points for question in questions])

    context = {
        'slug': slug,
        'total_points': total_points,
        'num_questions': num_questions,
        'questions': questions,
        'choices': choices,
        'error_message': "You didn't select a choice.",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template_name, context=context)


# def game(request, slug):
#     questions = Question.objects.filter(quiz__slug=slug)
#     choices = Choice.objects.filter(question__quiz__slug=slug).order_by('created')
#     total_points = sum([question.points for question in questions])
#     num_questions = questions.count()
#     # template_name = 'scoreboard/score_board.html'
#     template_name = 'trivia/game.html'
#     try:
#         selected_choices = questions.get(request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         context = {
#             'slug': slug,
#             'total_points': total_points,
#             'num_questions': num_questions,
#             'questions': questions[:1],
#             'choices': choices,
#             'error_message': "You didn't select a choice.",
#         }
#         return render(request, template_name, context=context)
#     else:
#         if selected_choices.correct:
            
#             # Always return an HttpResponseRedirect after successfully dealing
#             # with POST data. This prevents data from being posted twice if a
#             # user hits the Back button.
#             return HttpResponseRedirect(reverse('highscore'))


