from django.urls import path

from . import views

urlpatterns = [
    # ex: /locations/
    path('', views.index, name='index'),
    # ex: /locations/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /locations/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /locations/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
