from django.db import models
from time import *
# Create your models here.
class detail(models.Model):
    objects = None
    scheme=models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    mainxpath=models.CharField(max_length=70)
    xapth=models.CharField(max_length=70)
    field=models.CharField(max_length=70)
    created_at=models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=False)






