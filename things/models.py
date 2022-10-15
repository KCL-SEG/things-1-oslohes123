from django.db import models

# Create your models here.
class Thing(models.Model):
    first_name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    quantity = models.IntegerField()
