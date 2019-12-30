from rest_framework import serializers

from trivia.models import Exam, Question

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'user']

class QuestionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'option1', 'option2',
                  'option3', 'option4', 'answer', 'exam']
