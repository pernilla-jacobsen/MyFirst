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
    
    
    def get_absolute_url(self):
        return reverse('cat-detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    
