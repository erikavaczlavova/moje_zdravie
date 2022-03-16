from django.db import models

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text

class User(models.Model):
    name = models.CharField(max_length=200)
    birthnum = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    birthdate = models.DateTimeField('date of birth')
    weight = models.IntegerField()
    height = models.IntegerField()
