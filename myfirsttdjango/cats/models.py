from django.db import models


class Cat(models.Model):
    favorite_toy = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    picture_url = models.URLField(blank=True)   

    def __str__(self):
        return f"{self.name}, {self.age} years old, Breed: {self.breed}"
    
    def get_picture(self):
        return self.picture_url if self.picture_url else "No picture available."
    
    def play(self):
        return f"{self.name} is playing with {self.favorite_toy}!"
    
    def meow(self):
        return "Meow! Meow!"
    

    
