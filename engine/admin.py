from django.contrib import admin
from .models import Asset, Order, BuyOrder, SellOrder, Transaction

# Register your models here.
admin.site.register(Asset)
admin.site.register(BuyOrder)
admin.site.register(SellOrder)
admin.site.register(Transaction)