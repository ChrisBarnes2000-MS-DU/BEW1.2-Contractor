from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from trivia.models import Question, Choice
# from trivia.forms import QuizForm
from locations.models import Page

def trivia(request, slug):
    """View function for home page of TRIVIA."""
    template_name = 'trivia/game.html'

    # Generate counts of some of the main objects
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
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template_name, context=context)


# # /trivia/san-francisco/ with "san-francisco" being the quiz slug.
# def render_quiz(request, slug):
#     template_name = 'trivia/game.html'
#     quiz = get_object_or_404(Page, slug)
#     form = QuizForm(questions=quiz.question_set.all())
#     if request.method == "POST":
#         form = QuizForm(request.POST, questions=quiz.question_set.all())
#         if form.is_valid():  # Will only ensure the option exists, not correctness.
#             attempt = form.save()
#             return redirect(attempt)
#     return render(request, template_name, {"form": form})








# def answer(request, slug):
#     exam = get_object_or_404(Page, slug=slug)
#     try:
#         selected_choices = exam.choice_set.get(slug=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'trivia/game.html', {
#             'exam': exam,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choices.
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