from django.contrib import admin
from trivia.models import Exam, Question

admin.site.register(Exam)
admin.site.register(Question)

# from trivia.models import Quiz, Question, Answers

# class AnswersInline(admin.TabularInline):
#     model = Answers

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [AnswersInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

# class QuestionsInline(admin.TabularInline):
#     model = Question

# class QuizAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['quiz_tittle']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [QuestionsInline]
#     list_display = ('quiz_tittle', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['quiz_tittle']

# admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Question, QuestionAdmin)
