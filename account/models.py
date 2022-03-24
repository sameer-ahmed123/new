from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Shipment(models.Model):
    # user = models.ForeignKey(, on_delete=models.CASCADE)
    pickupTime = models.DateTimeField()
    userLocation = models.CharField(max_length=100,default='',blank=False)
    NoOfBoxes = models.IntegerField(default=0)
    recieverLocation = models.CharField(max_length=100,default='',blank=False)
    recievername = models.CharField(max_length=100,default='',blank=False)
    recieverphone = models.CharField(max_length=50,default='',blank=False)
    # status = models.BooleanField(default=False)
    CHOICES = (
        ('Ready_for_pickup', 'Ready_for_pickup'),
        ('pickedup', 'pickedup'),
        ('In_cargo', 'In_cargo'),
        ('reached_destination', 'reached_destination'),
        ('delivered', 'delivered'),

    )
    statuses = models.CharField(max_length=50, choices=CHOICES,default='')
    def __str__(self):
        return self.recievername

    def Cost_In_Dollars(self):
        return self.NoOfBoxes*2



class Employee(Shipment):
    pass