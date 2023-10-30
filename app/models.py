from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=250)
    user_type = models.CharField(max_length=250,null=True,blank=True)


class Doctor(models.Model):
    drname = models.CharField(max_length=250)
    daytime = models.TimeField()
    date =models.DateField()
    speciality = models.CharField(max_length=250)
    