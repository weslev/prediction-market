from django.contrib import admin
from .models import Event, Knowledge, Player, Share, Order, OrderLog, Transaction

# Register your models here.
admin.site.register(Event)
admin.site.register(Knowledge)
admin.site.register(Player)
admin.site.register(Share)
admin.site.register(Order)
admin.site.register(OrderLog)
admin.site.register(Transaction)