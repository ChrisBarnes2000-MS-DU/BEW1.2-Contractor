from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from trivia.views import trivia

urlpatterns = [
    # ex: /trivia/san-francisco/
    path('<str:slug>/', trivia, name='trivia'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
