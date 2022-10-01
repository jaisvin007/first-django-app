from django.db import models

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Product(models.Model):
    name=models.CharField(max_length=100)
    age= models.IntegerField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)