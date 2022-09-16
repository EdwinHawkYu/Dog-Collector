from django.db import models

# Create your models here.

class Dog:
    def __init__(self, name, breed, description, weight):
        self.name = name
        self.breed = breed
        self.description = description
        weight = weight

dogs = [
    Dog('Greg','Sheppard','Older dog',80),
    Dog('Jimbo','Doberman','Smart and trained doggie',75),
    Dog('Bailey','Poodle','Silly Dog',60)
]

