from django.db import models

# Create your models here.
#new model class
class Products(models.Model):
    # define a string field of max 100 characters
    prodname = models.CharField(max_length=100)
    # define a age that is an integer
    quantity = models.IntegerField()
    price = models.IntegerField()
    money = models.DecimalField(max_digits= 9, decimal_places=2, null =True)
    image = models.CharField(max_length = 500, null=True, blank=True)
    country = models.CharField(max_length=100, null= True, blank= True)

class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
