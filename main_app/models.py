from django.db import models

# Create your models here.
class Pin(models.Model):
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.brand