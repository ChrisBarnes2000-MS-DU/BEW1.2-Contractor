from django.contrib import admin
from locations.models import Page
from trivia.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'points', 'author', 'created', 'modified')
    list_filter = ['quiz', 'created']
    search_fields = ['quiz', 'content', 'author']

admin.site.register(Question, QuestionAdmin)