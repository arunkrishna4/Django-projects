from django.db import models

# Create your models here.
class Noobs(models.Model):
    name=models.CharField(max_length=200)
    pno =models.CharField( max_length=50)
    add =models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name