from django.db import models

# Create your models here.

class bot(models.Model):
    
   name = models.CharField(max_length=100)
   lastname = models.TextField(max_length=50)

