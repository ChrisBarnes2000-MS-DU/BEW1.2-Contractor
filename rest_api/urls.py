from django.urls import path, re_path

from rest_api.views import PageList, PageDetail, QuestionsList, ChoiceList
from scoreboard.views import ScoresView, ScoresAroundMeView

urlpatterns = [
    path("", PageList.as_view(), name="Page_list"),
    path("<int:pk>/", PageDetail.as_view(), name="Page_detail"),
    # path("<str:slug>/", PageDetail.as_view(), name="Page_detail"),
    path("All_Questions/", QuestionsList.as_view(), name="Questions_list"),
    path("All_Choices/", ChoiceList.as_view(), name="Choice_list"),

    # Api urls
    #url(r'^$', ScoresView.as_view(), name='leaderboard_api'),
    re_path(r'^api/(?P<game>[\w.@+-]+)/user/(?P<user_id>[\w.@+-]+)/',
            ScoresAroundMeView.as_view(), name='leaderboard_around_me_api'),
    re_path(r'^api/(?P<game>[\w.@+-]+)/$',
            ScoresView.as_view(), name='leaderboard_api'),
    re_path(r'^api/(?P<game>[\w.@+-]+)/(?P<page>[0-9]+)/$',
            ScoresView.as_view(), name='leaderboard_api_with_page'),
]
