from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from trivia.views import index, detail, results, vote

from django.conf.urls import url, include
from trivia import views

from rest_framework import routers

from trivia.views import ExamQuestionViewset, QuestionViewset, ExamViewset

router = routers.DefaultRouter()
router.register(r'question', QuestionViewset)
router.register(r'exam', ExamViewset)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.welcome, name="welcome"),
    url(r'^create/', views.create_user, name="create_user"),
    url(r'^validate_login/', views.log_in, name="log_user"),
    url(r'^add_exam/', views.add_exam, name="add_exam"),
    url(r'^add_question/', views.add_question, name="add_question"),
    url(r'^test', views.get_data, name="getdata"),
    url(r'^logout', views.log_out, name="log_out"),

    # # ex: /quiz/
    # path('', index, name='index'),
    # # ex: /quiz/5/
    # path('<int:question_id>/', detail, name='detail'),
    # # ex: /quiz/5/results/
    # path('<int:question_id>/results/', results, name='results'),
    # # ex: /quiz/5/votes/
    # path('<int:question_id>/votes/', vote, name='votes'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
