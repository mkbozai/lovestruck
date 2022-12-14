from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.


class Location(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  phone_num = models.CharField(max_length=14)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  category = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self): 
    return f'Name: {self.name}, ({self.id})'

  def get_absolute_url(self):
    return reverse('location_detail', kwargs={'pk': self.id})


class Partner(models.Model):
  name = models.CharField(max_length=100)
  notes = models.TextField(max_length=1000, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'Name: {self.name}, ({self.id})'

  def get_absolute_url(self):
    return reverse('partner_detail', kwargs={'pk': self.id})


class Date(models.Model):
  activity = models.CharField(max_length=200)
  budget = models.PositiveIntegerField(null=True)
  rating = models.PositiveIntegerField(null=True)
  date = models.DateField()
  notes = models.TextField(max_length=1000, blank=True)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'Date: {self.activity} ({self.id})'

  def get_absolute_url(self):
    return reverse('date_detail', kwargs={'pk': self.id})

  class Meta:
    ordering = ['-date']
