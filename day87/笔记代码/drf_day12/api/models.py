from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile=models.CharField(max_length=32,unique=True)  #唯一
    icon=models.ImageField(upload_to='icon',default='icon/default.png')  #需要配media文件夹,上传的文件就会放到media文件夹下的icon


class Book(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name