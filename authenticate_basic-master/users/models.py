from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Task(models.Model):
    nickname = models.CharField(max_length=100)
    task_complited = models.IntegerField()

class Support(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    text = models.TextField(blank=False)