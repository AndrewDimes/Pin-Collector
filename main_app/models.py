from django.db import models
from django.urls import reverse

# Create your models here.


class Pin(models.Model):
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.brand
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pin_id': self.id})
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    pins = models.ManyToManyField(Pin)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('categories_detail', kwargs={'category_id': self.id})

REACTIONS = (
    ('O', 'Love'),
    ('L', 'Like'),
    ('D', 'Dislike'),
    ('H', 'Hate')
)

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    reaction = models.CharField(
        max_length=1,
        choices=REACTIONS,
        default=REACTIONS[0][0]
    )
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_reaction_display()} - {self.comment}"