from django.db import models

# Create your models here.
class Potato(models.Model):
  brand = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  rating = models.IntegerField()

  def __str__(self):
    return self.brand