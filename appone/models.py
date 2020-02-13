from django.db import models

# Create your models here.

class StudInfo(models.Model):
    stname = models.CharField(max_length=100)
    stadr = models.CharField(max_length=100)
    stage = models.IntegerField()
    stfees = models.FloatField()
    active = models.CharField(max_length=100,default='Y')


class Address(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    active = models.CharField(max_length=100,default='Y')
