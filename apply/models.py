from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField(max_length=20)
    studentId = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)
    major = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)

    motive = models.TextField(max_length=499)
    position = models.CharField(max_length=10)
    positionRe = models.TextField(max_length=499)
    teamwork = models.TextField(max_length=499)
    passion = models.TextField(max_length=499)
    code = models.TextField(max_length=499)