from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=100,null=True)
    dob=models.DateField()
    emailid=models.EmailField(max_length=200)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=25)

class Contributor(models.Model):
    name=models.CharField(max_length=200,null=True)
    dob=models.DateField()
    emailid=models.EmailField(max_length=200)
    phone=models.CharField(max_length=10)
    designation=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=25)
