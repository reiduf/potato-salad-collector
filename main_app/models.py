from django.db import models
from django.urls import reverse

# Create your models here.
class Potato(models.Model):
  brand = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  rating = models.IntegerField()

  def __str__(self):
    return self.brand
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'potato_id': self.id})