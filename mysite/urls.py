"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from mysite.views import Index, About

urlpatterns = [
    # Index Page
    path('', Index, name='index'),

    # About Page
    path('about/', About, name='about'),

    # Accounts app
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Admin Site
    path('admin/', admin.site.urls),

    # API
    path('api/', include('rest_api.urls')),

    # Contact
    path('contact/', include('contact.urls')),

    # Locations App
    path('locations/', include('locations.urls')),

    # trivia App
    path('trivia/', include('trivia.urls')),

    #High score page
    path('highscores/', include('scoreboard.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
