from django.db import models
from django.contrib.auth.models import User

#######################
#Quiz Structure Models#
#######################

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    creation = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name

    def possible(self):
        total = 0
        for question in self.question_set.all():
            question.save()
            total += question.value
        return total

class Question(models.Model):
    question = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    creation = models.DateField(auto_now_add=True)
    #objective = TODO: include standards linking in later versions
    value = models.IntegerField(default=1)

    def __unicode__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    #Creator is tied to the quiz

##########
#Attempts#
##########
class QuizAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    #Score Method (similar to possible in Quiz

class QuestionAttempt(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Answer, on_delete=models.PROTECT)




# from django.contrib.auth.models import User
# from django.utils import timezone
# from locations.models import Page
# from django.conf import settings
# from django.db import models
# import datetime

# class Question(models.Model):
#     """ Represents a question. """
#     objects = models.Manager()
#     quiz = models.ForeignKey(Page, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.PROTECT, help_text="The user that posted this question.")

#     created = models.DateTimeField(auto_now_add=True, help_text="The date&time this question was created. Automatically generated when the model saves.")
#     modified = models.DateTimeField(auto_now=True, help_text="The date&time this question was updated. Automatically generated when the model updates.")

#     points = models.IntegerField(default=10, help_text="number of points given for getting the correct answer to this question")
#     content = models.TextField(default="Write the content of your question here.")

#     def __str__(self):
#         return self.content

# class Choice(models.Model):
#     """ Represents a question. """
#     objects = models.Manager()
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add=True, help_text="The date&time this question was created. Automatically generated when the model saves.")
#     modified = models.DateTimeField(auto_now=True, help_text="The date&time this question was updated. Automatically generated when the model updates.")

#     content = models.TextField(max_length=200, default="Write the content of your question here.",)
#     correct = models.BooleanField(default=False, help_text="Is this the correct answer")

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.created <= now
#     was_published_recently.admin_order_field = 'created'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'

#     def __str__(self):
#         return self.content
