from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.

EXPERIENCE = (
    ('B', 'Beginner'),
    ('I', 'Intermeidate'),
    ('E', 'Expert')
)

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    weight = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id':self.id})

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    experience = models.CharField(
        max_length=1,
        choices=EXPERIENCE,
        default=EXPERIENCE[0][0]
        )
    
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']

