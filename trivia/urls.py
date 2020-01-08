from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import trivia

urlpatterns = [
    # ex: /trivia
    path('', trivia, name='trivia'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
