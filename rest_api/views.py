from rest_framework import generics

from locations.models import Page
from trivia.models import Question, Choice
from rest_api.serializer import PageSerializer, QuestionSerializer, ChoiceSerializer

class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(generics.RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class QuestionsList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
