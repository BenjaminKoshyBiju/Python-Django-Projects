from django.db import models

# Create your models here.
class destination(models.Model):
    price= models.IntegerField(default=0)
    img=models.ImageField(upload_to='img', null=True)
    desc=models.TextField()
    name=models.CharField(max_length=200)
    offer=models.BooleanField(default=False)
