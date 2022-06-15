from django.db import models
from django import forms
from django.contrib.auth.models import User


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
        return f'{self.title} - {self.slug}'
'''
class Waiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True) #models.ManyToManyField(Cafe, blank=True)
    def __str__(self):
        return self.user.username #({self.user.name})'
'''

class WaiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True) #models.ManyToManyField(Cafe, blank=True)
    def __str__(self):
        return self.user.username #({self.user.name})'



