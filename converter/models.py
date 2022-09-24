#!user/bin/python3
from django.db import models
import uuid
# Create your models here.


class signup(models.Model):
    User_Id = models.AutoField(primary_key=True)
    User_name = models.TextField()
    Password = models.TextField()
    Profile_Img = models.TextField()

    
class converter(models.Model):
    Todo_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Todo = models.TextField(default='USD')
    Done = models.CharField(max_length=(400),default="hello")
    
    
