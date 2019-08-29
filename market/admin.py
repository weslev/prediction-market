from django.contrib import admin
from .models import Asset, Share, Trader

# Register your models here.
admin.site.register(Asset)
admin.site.register(Share)
admin.site.register(Trader)