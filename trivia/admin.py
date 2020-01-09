from django.contrib import admin
from locations.models import Page
from trivia.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'multiple', 'points', 'created', 'modified')
    list_filter = ['quiz', 'created', 'multiple']
    search_fields = ['quiz', 'content', 'multiple']

admin.site.register(Question, QuestionAdmin)