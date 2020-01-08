import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    """ Represents a quiz/exam. """
    objects = models.Manager()
    created = models.DateTimeField(auto_now_add=True, help_text="The date&time this exam was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date&time this exam was updated. Automatically generated when the model updates.")
    title = models.CharField(max_length=settings.PAGE_TITLE_MAX_LENGTH, unique=True, default="Title of your exam.")
    author = models.ForeignKey(User, on_delete=models.PROTECT, help_text="The user that posted this exam.")

    def __str__(self):
        return self.title

class Question(models.Model):
    """ Represents a question. """
    objects = models.Manager()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, help_text="The date&time this question was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date&time this question was updated. Automatically generated when the model updates.")
    content = models.TextField(default="Write the content of your question here.")
    author = models.ForeignKey(User, on_delete=models.PROTECT, help_text="The user that posted this exam.")

    def __str__(self):
        return self.content
