from django.db import models
from django import forms
import uuid
from django.contrib.auth.models import User
from datetime import datetime


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Cafe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class WaiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', default=0, blank=True, unique=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True) #models.ManyToManyField(Cafe, blank=True)
    #balance = models.FloatField(default=0)
    def __str__(self):
        return self.user.username #({self.user.name})'

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=200, unique=True,  blank=True)
    image = models.ImageField(upload_to='images', default=0, blank=True)
    def __str__(self):
        return self.user.username #({self.user.name})'


class Join(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    cafe = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    message = models.TextField(blank=True, default="No additional information")
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.email


class Transaction(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.now)
    tID = models.CharField(max_length=200, unique=True, default=uuid.uuid4)
    amount = models.FloatField(default=0)
    comment = models.TextField(blank=True, default="No additional information")
    def __str__(self):
        return self.tID