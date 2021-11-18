from django.db import models

# Create your models here.
#new model class
class Products(models.Model):
    # define a string field of max 100 characters
    prodname = models.CharField(max_length=100)
    # define a age that is an integer
    quantity = models.IntegerField()
    price = models.IntegerField()


class Todo(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
