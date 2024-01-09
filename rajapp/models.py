from django.db import models

class stud(models.Model):
    name=models.CharField(max_length=20,default="")
    password=models.CharField(max_length=20,default="")
    address=models.CharField(max_length=20,default="")
    contact=models.CharField(max_length=20,default="")
    email=models.CharField(max_length=30,default="")
