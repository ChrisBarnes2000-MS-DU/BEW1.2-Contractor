from django.contrib import admin
from locations.models import Page
from trivia.models import Question

class QuestionInline(admin.TabularInline):
    model = Question

class PageAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    inlines = [QuestionInline]
    list_display = ('title', 'slug', 'author', 'created', 'modified')
    list_filter = ['title', 'created']
    search_fields = ['title', 'author']

admin.site.register(Page, PageAdmin)
