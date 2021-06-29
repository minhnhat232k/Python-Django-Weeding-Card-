from django.db import models

# Create your models here.
class Subscribe(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    time = models.CharField(max_length=20)  
    day = models.CharField(max_length=20)  
    month = models.CharField(max_length=20)  
    year = models.CharField(max_length=20)  
    address = models.CharField(max_length=200)  
    class Meta:  
        db_table = "subscribe"  