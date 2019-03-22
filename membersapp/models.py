from django.db import models

# Create your models here.

class User(models.Model):
    """ Defines the layout for user """

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    attr = models.CharField(max_length=50)
