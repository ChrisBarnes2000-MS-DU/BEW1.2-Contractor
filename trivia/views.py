from django.shortcuts import render

def trivia(request):
    """View function for home page of TRIVIA."""
    template_name = 'trivia/game.html'

    # Generate counts of some of the main objects
    # num_questions = Question.objects.all().count()
    # page = Page.objects.get(Page.slug)

    context = {
        # 'num_questions': num_questions,
        'page': "Tittle",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, template_name, context=context)

def Score_board(request):
    template_name = 'trivia/score_board.html'
    context = {
        # 'num_questions': num_questions,
        'highscores': ['1','2','5','133','80'],
    }
    return render(request, template_name, context)
