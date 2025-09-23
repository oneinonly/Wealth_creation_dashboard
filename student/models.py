from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    education=models.CharField(max_length=50,default='')
    mobile=models.CharField(max_length=10,default='')
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    address=models.CharField(max_length=500,default='')
    bloodgroub=models.CharField(max_length=3, default='')
    photo=models.ImageField(upload_to='media', default='')

    def __str__(self):
        return self.name

class teachers(models.Model):   
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    subject=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class facalty(models.Model):   
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='media', default='')

    def __str__(self):
        return self.name