from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

EXPERIENCE = (
    ('B', 'Beginner'),
    ('I', 'Intermeidate'),
    ('E', 'Expert')
)

class Collar(models.Model):
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=50)

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    weight = models.IntegerField()
    collars = models.ManyToManyField(Collar)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

