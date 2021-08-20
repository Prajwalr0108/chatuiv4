from django.db import models

# Create your models here.
class bot(models.Model):
    
   input = models.CharField(max_length=100)
   output = models.CharField(max_length=100)

class new(models.Model):
   
    inputt = models.CharField(max_length=100)
    outputt = models.CharField(max_length=100)




    
