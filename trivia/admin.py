from django.contrib import admin
from trivia.models import Quiz, Question, Answer

#######
#Admin#
#######

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2

class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'creation', 'possible',)
    search_fields = ('name', 'creator')
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    search_fields = ('question', 'quiz', 'value',)
    list_display = ('question', 'quiz', 'value',)

admin.site.register(Question, QuestionAdmin)




# from django.contrib import admin
# from locations.models import Page
# from trivia.models import Question

# class QuestionInline(admin.TabularInline):
#     model = Question

# class PageAdmin(admin.ModelAdmin):
#     """ Show helpful fields on the changelist page. """
#     inlines = [QuestionInline]
#     list_display = ('title', 'slug', 'author', 'created', 'modified')
#     list_filter = ['title', 'created']
#     search_fields = ['title', 'author']

# admin.site.register(Page, PageAdmin)



# from django.contrib import admin
# from trivia.models import Question, Choice

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     # list_display = ('question', 'content', 'correct', 'created', 'modified')

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [ChoiceInline]
#     list_display = ('content', 'points', 'author', 'created', 'modified')
#     list_filter = ['quiz', 'created']
#     search_fields = ['quiz', 'content', 'author']

# admin.site.register(Question, QuestionAdmin)
