from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Cat(models.Model):
    favorite_toy = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    picture = models.ImageField(default='default_cat.jpg', upload_to='cat_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.age} years old, Breed: {self.breed}"
    
    def get_picture(self):
        return self.picture_url if self.picture_url else "No picture available."
    
    def play(self):
        return f"{self.name} is playing with {self.favorite_toy}!"
    
    def meow(self):
        return "Meow! Meow!"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    
