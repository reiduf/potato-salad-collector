from django.db import models
from django.urls import reverse

# Create your models here.
class Store(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('stores_detail', kwargs={'pk': self.id})

class Potato(models.Model):
  brand = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  rating = models.IntegerField()
  stores = models.ManyToManyField(Store)

  def __str__(self):
    return self.brand
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'potato_id': self.id})
  
class Comment(models.Model):
  date = models.DateField()
  comments = models.CharField(max_length=100)

  potato = models.ForeignKey(Potato, on_delete=models.CASCADE)
  def __str__(self):
    return f"On {self.date} you said {self.comments}"
  
  class Meta:
    ordering = ['-date']

