from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from trivia.views import index, add_exam, add_question, get_data, QuestionViewset, ExamViewset

router = routers.DefaultRouter()
router.register(r'question', QuestionViewset)
router.register(r'exam', ExamViewset)

urlpatterns = [
    # ex: /trivia/
    path('', index, name='trivia'),
    # ex: /api/
    path('api/', include(router.urls)),
    # ex: /trivia/create/
    # path('create/', create_user, name="create_user"),
    # ex: /trivia/validate_login/
    # path('validate_login/', log_in, name="log_user"),
    # ex: /trivia/add_exam/
    path('add_exam/', add_exam, name="add_exam"),
    # ex: /trivia/add_question/
    path('add_question/', add_question, name="add_question"),
    # ex: /trivia/test/
    path('test/', get_data, name="getdata"),
    # ex: /trivia/logout/
    # path('logout/', log_out, name="log_out"),

    # '<int:question_id>/', detail, name='detail'

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
