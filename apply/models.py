from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField(max_length=100)
    studentId = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    motive = models.TextField()
    position = models.CharField(max_length=10)
    positionRe = models.TextField()
    teamwork = models.TextField()
    passion = models.TextField()
    code = models.TextField()