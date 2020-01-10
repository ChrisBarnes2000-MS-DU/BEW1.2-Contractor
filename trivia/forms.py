# from django import forms
# from locations.models import Page

# class QuizForm(forms.Form):
#     def __init__(self, data, questions, *args, **kwargs):
#         super(QuizForm, self).__init__(data, *args, **kwargs)
#         self.questions = questions
#         for question in questions:
#             # question_num = "question_%d" % question.pk
#             choices = []
#             for answer in question.answer_set().all():
#                 choices.append((answer.pk, answer.answer,))
#             ## May need to pass some initial data, etc:
#             field = forms.ChoiceField(label=question.content, required=True,
#                                       choices=choices, widget=forms.RadioSelect)

#     def save(self):
#         ## Loop back through the question/answer fields and manually
#         ## update the Attempt instance before returning it.
#         pass
