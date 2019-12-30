import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Exam(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, default="Exam Name")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name

class Question(models.Model):
    objects = models.Manager()
    question = models.TextField(max_length=200, default="")
    option1 = models.CharField(max_length=50, default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default="Exam Name")

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
