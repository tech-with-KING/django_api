#!user/bin/python3
from django.db import models

# Create your models here.


class converter(models.Model):
    currency = models.TextField()

