from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the Locations index.")

"""
def index(request):
    latest_question_list = Question.objects.get('-pub_date')
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
"""

# class index(ListView):
#     """ Renders a list of all Pages. """
#     model = Question

#     def get(self, request):
#         """ GET a list of Pages. """
#         pages = self.get_queryset().all()
#         return render(request, 'list.html', {'pages': pages})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
