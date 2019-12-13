# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from contact.views import emailView, successView

urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]