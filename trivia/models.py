import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from locations.models import Page

class Question(models.Model):
    """ Represents a question. """
    objects = models.Manager()
    quiz = models.ForeignKey(Page, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, help_text="The user that posted this question.")

    created = models.DateTimeField(auto_now_add=True, help_text="The date&time this question was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date&time this question was updated. Automatically generated when the model updates.")

    points = models.IntegerField(default=10, help_text="number of points given for getting the correct answer to this question")
    content = models.TextField(default="Write the content of your question here.")

    def __str__(self):
        return self.content

class Choice(models.Model):
    """ Represents a question. """
    objects = models.Manager()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, help_text="The date&time this question was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date&time this question was updated. Automatically generated when the model updates.")

    content = models.TextField(default="Write the content of your question here.")
    correct = models.BooleanField(default=False, help_text="Is this the correct answer")

    def __str__(self):
        return self.content
