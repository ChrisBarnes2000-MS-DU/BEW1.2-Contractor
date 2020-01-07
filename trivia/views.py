from django.shortcuts import render
from django.http import HttpResponse

def trivia(request):
    return HttpResponse("Hello, world. You're at the Triva index.")
