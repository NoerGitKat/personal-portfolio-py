from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    description = models.CharField(max_length=200)
