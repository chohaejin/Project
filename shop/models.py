from django.db import models

# Create your models here.
class Good(models.Model):
    name = models.TextField()
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images/', blank=False)