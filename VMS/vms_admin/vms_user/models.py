# models.py
from django.db import models

class Phase(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Building(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Visitor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    PURPOSE_CHOICES = [
        ('Business', 'Business'),
        ('Tourism', 'Tourism'),
        ('Work', 'Work'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    place = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='visitor_photos/')
    visit_time = models.TimeField()
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    visit_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return f"Visitor {self.name} ({self.id})"
