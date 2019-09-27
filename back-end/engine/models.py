from django.db import models
from datetime import datetime  

class Event(models.Model):
	name = models.CharField(max_length=300)
	ground_truth = models.FloatField()

class Knowledge(models.Model):
	value = models.BooleanField(default=False)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	index = models.IntegerField()

class Player(models.Model):
	name = models.CharField(max_length=300)
	capital = models.FloatField()
	#001
	local_info = models.ManyToManyField(Knowledge)
	events = models.ManyToManyField(Event)

class Share(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	asset = models.BooleanField(default=False)
	owner = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
	price = models.FloatField(default=0)

class Order(models.Model):
	#django has automatic timestamp
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	price = models.FloatField()
	status = models.BooleanField(default=True)
	closingTime = models.DateTimeField(null=True, blank=True)
	#buy (1) or sell (0)
	side = models.BooleanField(default=False)
	#for sell orders, check for shares owned by me
	order_type = models.BooleanField(default=False)

class OrderLog(models.Model):
	#django has automatic timestamp
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	price = models.FloatField()
	closingTime = models.DateTimeField(null=True, blank=True)
	#buy (1) or sell (0)
	side = models.BooleanField(default=False)
	#for sell orders, check for shares owned by me
	order_type = models.BooleanField(default=False)

class Transaction(models.Model):
	share = models.ForeignKey(Share, on_delete=models.CASCADE)
	buyer = models.ForeignKey(Player, related_name="buyer", on_delete=models.CASCADE)
	seller = models.ForeignKey(Player, related_name="seller", on_delete=models.CASCADE)
	price = models.FloatField()



