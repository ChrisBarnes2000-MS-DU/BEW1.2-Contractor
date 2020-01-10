from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from trivia.views import trivia
# , grade

urlpatterns = [
    # ex: /trivia/san-francisco/
    path('<str:slug>/', trivia, name='trivia'),
    # path('<str:slug>/', grade, name='grade')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
