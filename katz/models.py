from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateTimeField('Date of Birth')


class Customer(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
# Create your models here.
