from django.contrib import admin
from trivia.models import Question

class QuestionAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('content', 'author', 'created', 'modified')

admin.site.register(Question, QuestionAdmin)
