from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from trivia.models import Question, Answer
from locations.models import Page

def trivia(request, slug):
    """View function for home page of TRIVIA."""
    template_name = 'trivia/game.html'

    # Generate counts of some of the main objects
    questions = Question.objects.filter(quiz__slug=slug)
    choices = Answer.objects.filter(question__quiz__slug=slug).order_by('created')
    num_questions = questions.count()

    context = {
        'slug': slug,
        'num_questions': num_questions,
        'questions': questions,
        'choices': choices,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template_name, context=context)

# def answer(request, slug):
#     exam = get_object_or_404(Page, slug=slug)
#     try:
#         selected_choices = exam.choice_set.get(slug=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'location/page.html', {
#             'exam': exam,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('trivia:results', args=(slug,)))

# class ResultsView(generic.DetailView):
#     model = Page
#     template_name = 'polls/results.html'

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())

def Score_board(request):
    template_name = 'trivia/score_board.html'
    context = {
        'highscores': ['1','2','5','133','80'],
    }
    return render(request, template_name, context)
