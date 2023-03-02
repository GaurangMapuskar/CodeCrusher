from django.db import models
class farmers(models.Model):
    name=models.CharField(null=True, max_length=50)
    address=models.TextField()
    contact=models.IntegerField()
    email=models.EmailField(null=True, max_length=254)

class request(models.Model):
    trucktype=models.CharField(null=True, max_length=50)
    quantity=models.IntegerField()
    products=models.CharField(null=True, max_length=50)
    destination=models.CharField(null=True, max_length=50)
    accept=models.BooleanField(default=False)
    
class truckers(models.Model):
    trucktype=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    contact=models.IntegerField()
    email=models.EmailField( max_length=254)
