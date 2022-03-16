from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    birthnum = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    birthdate = models.DateTimeField('date of birth')
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name

class Test(models.Model):
    user_id = models.IntegerField()
    date = models.DateTimeField('date of birth')
    result = models.BooleanField()
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)


    # def __str__(self):
    #     return self.name

class Vaccine(models.Model):
    user_id = models.IntegerField()
    date = models.DateTimeField('date of birth')
    dose = models.IntegerField()
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name

class Passport(models.Model):
    user_id = models.IntegerField()
    vaccine_id = models.IntegerField()
    date = models.DateTimeField('date of birth')
    dose = models.IntegerField()
    name = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name