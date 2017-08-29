from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.ForeignKey(User, null=True)
    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()

    commented_on = models.ForeignKey(Book)
    in_reply_to = models.ForeignKey('self', null=True)

    commented_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)