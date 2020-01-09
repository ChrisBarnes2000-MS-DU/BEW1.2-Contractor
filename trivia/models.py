from django.contrib.auth.models import User
from django.utils import timezone
from locations.models import Page
from django.conf import settings
from django.db import models
import datetime

class Question(models.Model):
    """ Represents a question. """
    objects = models.Manager()
    quiz = models.ForeignKey(Page, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, help_text="The date&time this question was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date&time this question was updated. Automatically generated when the model updates.")

    multiple = models.BooleanField(default=False, help_text="Is this the multiple choice answer")
    points = models.IntegerField(default=10, help_text="number of points given for getting the correct answer to this question")
    content = models.CharField(max_length=200, default="Write the content of your question here.")

    def __str__(self):
        return self.content

class Choice(models.Model):
    """ Represents a question. """
    objects = models.Manager()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, help_text="The date&time this question was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date&time this question was updated. Automatically generated when the model updates.")

    content = models.CharField(max_length=200, default="Write the content of your question here.",)
    correct = models.BooleanField(default=False, help_text="Is this the correct answer")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now
    was_published_recently.admin_order_field = 'created'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.content
