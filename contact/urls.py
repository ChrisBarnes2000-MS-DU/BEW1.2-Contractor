# contact/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from contact.views import emailView, successView

urlpatterns = [
    path('', emailView, name='email'),
    path('success/', successView, name='success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
