from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    birthnum = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    birthdate = models.DateTimeField('date of birth')
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date of the test')
    result = models.BooleanField(null=True, blank=True)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.user.name + self.location + self.type

class Vaccine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date of vaccination')
    dose = models.IntegerField()
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)

    def __str__(self):
        return self.user.name + str(self.dose)

class Passport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vaccine)


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.FileField(upload_to='files/')
