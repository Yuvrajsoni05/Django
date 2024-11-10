from django.db import models

# Create your models here.

class AllModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    event_time = models.TimeField()
    file = models.FileField(upload_to='uploads/')
    image = models.ImageField(upload_to='images/')
    email = models.EmailField()
    website = models.URLField()

    COLOR_CHOICES = [
        ('R', 'Red'),
        ('G', 'Green'),
        ('B', 'Blue'),
    ]
    favorite_color = models.CharField(max_length=1, choices=COLOR_CHOICES)


