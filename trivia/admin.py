from django.contrib import admin
from trivia.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('quiz', 'content', 'points', 'author', 'created', 'modified')

class ChoiceAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('question', 'content', 'correct', 'created', 'modified')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
