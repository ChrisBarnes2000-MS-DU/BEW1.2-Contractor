from django.shortcuts import render
from trivia.models import Question

def trivia(request, slug):
    """View function for home page of TRIVIA."""
    template_name = 'trivia/game.html'

    # Generate counts of some of the main objects
    num_questions = Question.objects.all().count()
    # page = Page.objects.get(Page.slug)

    context = {
        'slug': slug,
        'num_questions': num_questions,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template_name, context=context)

def Score_board(request):
    template_name = 'trivia/score_board.html'
    context = {
        'highscores': ['1','2','5','133','80'],
    }
    return render(request, template_name, context)
