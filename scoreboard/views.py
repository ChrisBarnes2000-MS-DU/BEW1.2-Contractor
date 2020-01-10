from django.contrib.auth.models import User
from django.template import RequestContext
from scoreboard.forms import ScoreForm
from django.views.generic import View
from django.http import Http404
from leaderboard.leaderboard import Leaderboard
from django.shortcuts import render

def Score_board(request):
    template_name = 'scoreboard/score_board.html'
    context = {
        'highscores': ['1', '2', '5', '133', '80'],
    }
    return render(request, template_name, context)

def highscores(request, game="trivia", page=1):
    """
    displays the scoreboard table
    """
    template_name = 'scoreboard/highscores.html'
    # You can set the default page size
    #Leaderboard.DEFAULT_PAGE_SIZE = 2
    page = int(page)
    scoreboard = Leaderboard(game)
    scores = scoreboard.leaders(int(page))
    if not scores:
        scores = []
    total_pages = int(scoreboard.total_pages())

    # Pagination values
    has_next = True if (page < total_pages) else False
    has_prev = True if (page != 1) else False
    next_page = page + 1 if has_next else page
    prev_page = page - 1 if has_prev else page

    # hashmap to get the score instance quickly
    score_list = {}

    # Collect the user ids
    user_ids = []
    for score in scores:
        user_ids.append(score["member"])
        score_list[int(score["member"])] = score

    # Fetch users in question
    users = User.objects.filter(pk__in=user_ids)

    for user in users:
        score_list[user.pk]["user"] = user

    context = {
        'scores': scores,
        'total_pages': total_pages,
        'game': game,
        'page': page,
        'has_next': has_next,
        'has_prev': has_prev,
        'next_page': next_page,
        'prev_page': prev_page,
    }

    return render(request, template_name, context=context)

class ScoresView(View):
    """
    The resource to manage scores on the scoreboard
    """

    form = ScoreForm

    def get(self, request, game, page=1):
        """
        Returns the high scores
        @todo: pagination
        """
        scoreboard = Leaderboard(game)
        scores = scoreboard.leaders(int(page))
        total_pages = scoreboard.total_pages()
        return {
            "meta":
                {
                    "total_pages": int(total_pages)
                },
                "scores": scores if scores else []
        }

    def post(self, request, game, page=1):
        """
        Creates new rankings

        Params:
            game: game identifier
            user_id: pk of the user
            score: positive integer

        Returns:
            1 on creation, 0 on updation
        """
        user_id = request.POST.get('user_id')
        score = request.POST.get('score')

        try:
            user = User.objects.get(pk=user_id)
        except:
            return Http404('User Not Found')

        scoreboard = Leaderboard(game)
        status = scoreboard.rank_member(user.id, int(score))
        return {"status": status}

    def delete(self, request, game, page=1):
        """
        deletes the score
        """
        pass


class ScoresAroundMeView(View):
    def get(self, request, game, user_id):
        """
        Returns the scores around the user
        """
        scoreboard = Leaderboard(game)
        scores = scoreboard.around_me(user_id)

        return {
            "meta": {},
            "scores": scores if scores else []
        }
