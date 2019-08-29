from django.db import models
from datetime import datetime  

# Create your models here.
class Asset(models.Model):
	name = models.CharField(max_length=300)

class Order(models.Model):
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
	size = models.IntegerField()
	status = models.BooleanField(default=False)
	start = models.DateTimeField(auto_now_add=True)
	end = models.DateTimeField(null=True, blank=True)

class BuyOrder(Order):
	bid = models.FloatField()

class SellOrder(Order):
	ask = models.FloatField()

class Transaction(models.Model):
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
	bid = models.ForeignKey(BuyOrder, on_delete=models.CASCADE)
	ask = models.ForeignKey(SellOrder, on_delete=models.CASCADE)
	price = models.FloatField()
	size = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)

