from django.urls import path

from locations.views import PageListView, PageCreateView, PageDetailView, PageEditView, detail, results, vote

urlpatterns = [
    path('', PageListView.as_view(), name='list-page'),
    path('new/', PageCreateView.as_view(), name='create-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='details-page'),
    path('<str:slug>/edit/', PageEditView.as_view(), name='edit-page'),

    # ex: /locations/
    # path('', index, name='index'),
    # ex: /locations/5/
    path('<int:question_id>/', detail, name='detail'),
    # ex: /locations/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /locations/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
]
