from django.db import models

# Create your models here.

class Project(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.CharField(max_length=20)
    
