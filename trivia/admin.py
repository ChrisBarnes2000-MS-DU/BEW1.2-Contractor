from django.contrib import admin
from trivia.models import Exam, Question

class ExamAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'author', 'created', 'modified')


class QuestionAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('content', 'author', 'created', 'modified')


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
