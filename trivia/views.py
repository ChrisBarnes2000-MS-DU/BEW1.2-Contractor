from django.shortcuts import render
from trivia.models import Question, Choice

def trivia(request, slug):
    """View function for home page of TRIVIA."""
    template_name = 'trivia/game.html'

    # Generate counts of some of the main objects
    questions = Question.objects.filter(quiz__slug=slug)
    choices = Choice.objects.filter(question__quiz__slug=slug)
    num_questions = questions.count()

    context = {
        'slug': slug,
        'num_questions': num_questions,
        'questions': questions,
        'choices': choices,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template_name, context=context)

def Score_board(request):
    template_name = 'trivia/score_board.html'
    context = {
        'highscores': ['1','2','5','133','80'],
    }
    return render(request, template_name, context)
