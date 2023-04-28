from django.db import models
from django.urls import reverse

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
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'wine_id': self.id})
    
class SoldDate(models.Model):
    date = models.DateField('Sold Date')
    quantity = models.IntegerField(max_length=3, default=1)

    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_quantity_display()} on {self.date}"
