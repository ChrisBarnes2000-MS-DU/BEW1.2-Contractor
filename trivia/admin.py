from django.contrib import admin
from trivia.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    # list_display = ('question', 'content', 'correct', 'created', 'modified')

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'points', 'author', 'created', 'modified')
    list_filter = ['quiz', 'created']
    search_fields = ['quiz', 'content', 'author']

admin.site.register(Question, QuestionAdmin)
