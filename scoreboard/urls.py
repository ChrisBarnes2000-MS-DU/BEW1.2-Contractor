from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from scoreboard.views import highscores, Score_board

urlpatterns = [
    # ex: /scoreboard/
    # path('', highscores, name='highscore'),
    path('', Score_board, name='highscore'),

    # the leaderboard for the high scores
    re_path(r'^highscores/(?P<game>[\w.@+-]+)/$', highscores, name="leaderboard_high_scores"),
    re_path(r'^highscores/(?P<game>[\w.@+-]+)/(?P<page>[\w.@+-]+)/$', highscores, name="leaderboard_high_scores_with_page"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
