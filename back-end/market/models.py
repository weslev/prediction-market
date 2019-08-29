from django.db import models
from jsonfield import JSONField

# Create your models here.
class Asset(models.Model):
	name = models.CharField(max_length=300)
	ground_truth = models.CharField(max_length=10)


class Share(models.Model):
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
	direction = models.BooleanField(default=False)

class Trader(models.Model):
	username = models.CharField(max_length=300)
	capital = models.FloatField(default=0)


