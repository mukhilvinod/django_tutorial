from django.db import models

# Create your models here.
class new_user(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    place=models.CharField(max_length=200)