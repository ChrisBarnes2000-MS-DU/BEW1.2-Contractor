from django.urls import path

from .views import PageListView, detail, results, vote, index

urlpatterns = [
    # ex: /locations/
    # path('', index, name='index'),
    path('', PageListView.as_view(), name='list-page'),
    # ex: /locations/5/
    path('<int:question_id>/', detail, name='detail'),
    # ex: /locations/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /locations/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
]
