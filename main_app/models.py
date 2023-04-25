from django.db import models

# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=50)
    abv = models.FloatField(max_length=4)
    region = models.CharField(max_length=50)
    dryness = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    type = models.CharField(max_length=75)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.name
