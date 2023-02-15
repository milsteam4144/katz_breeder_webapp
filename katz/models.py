from django.db import models

# Create your models/classes/db tables here.
# https://docs.djangoproject.com/en/4.1/topics/db/models/
from django.db.models import UniqueConstraint


class Breeder(models.Model):
    breederID = models.AutoField(primary_key=True)
    breeder_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    cattery = models.CharField(max_length=60)
    location = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)

class Cat(models.Model):
    #class Meta:
        #UniqueConstraint(fields = ['id', 'breederId'], name = 'cat_name')
        id = models.AutoField(primary_key=True)
        breederId = models.ForeignKey(Breeder, on_delete=models.CASCADE)
        name = models.CharField(max_length=50)
        #birthdate = models.DateTimeField()
        color = models.CharField(max_length=20)
        catType = models.CharField(max_length=10)
        status = models.CharField(max_length=10)
        pattern  = models.CharField(max_length=20)
        gender  = models.CharField(max_length=1)
        mother = models.IntegerField()
        father = models.IntegerField()
        images = models.ImageField()
        personality = models.TextField()



class Customer(models.Model):
    customerID = models.AutoField()
    catID = models.ForeignKey(Cat, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    birthdate = models.DateField()
    address = models.TextField()

class Transaction(models.Model):
    transactionID = models.AutoField()
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    catID = models.ForeignKey(Cat, on_delete=models.CASCADE)
    type = models.CharField(max_length=15)
    date = models.DateField()

class Contract(models.Model):
    transactionID = models.IntegerField()
    image_file = models.ImageField()