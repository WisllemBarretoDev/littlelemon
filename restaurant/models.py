from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
    
