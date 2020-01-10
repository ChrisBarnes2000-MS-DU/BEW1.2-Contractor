from django.contrib import admin
from locations.models import Page
from trivia.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'points', 'multiple',  'created', 'modified')
    list_filter = ['quiz', 'created', 'multiple']
    search_fields = ['quiz', 'content', 'multiple']

admin.site.register(Question, QuestionAdmin)

class PageAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    inlines = [QuestionInline]
    list_display = ('title', 'slug', 'author', 'created', 'modified')
    list_filter = ['title', 'created']
    search_fields = ['title', 'author']

admin.site.register(Page, PageAdmin)
