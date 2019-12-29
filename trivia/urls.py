from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from trivia.views import index, detail, results, vote

urlpatterns = [
    # ex: /quiz/
    path('', index, name='index'),
    # ex: /quiz/5/
    path('<int:question_id>/', detail, name='detail'),
    # ex: /quiz/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /quiz/5/votes/
    path('<int:question_id>/votes/', vote, name='votes'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
