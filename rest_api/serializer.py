from rest_framework import serializers

from locations.models import Page
from trivia.models import Question, Choice

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"
