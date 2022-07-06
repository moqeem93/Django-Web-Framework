from django.db import models

# Create your models here.
class Students(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    email = models.EmailField()
    record = models.DateField(auto_created=True)
    date = models.DateTimeField(auto_now_add=True)
