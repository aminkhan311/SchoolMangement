from django.db import models
from datetime import datetime,date
# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Class=models.IntegerField()
    Mobile=models.IntegerField()
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    PinCode=models.IntegerField()
