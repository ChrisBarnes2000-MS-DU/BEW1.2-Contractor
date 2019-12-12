from django.contrib import admin
from locations.models import Page, Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class PageAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created', 'modified')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Page, PageAdmin)
