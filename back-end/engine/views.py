from django.shortcuts import render
from .models import BuyOrder, SellOrder, Asset
import json
from django.http import JsonResponse, HttpResponse


# Create your views here.
def order(request):
	r = json.loads(request.body)

	if r["orderType"] == "buy":
		assetID = Asset.objects.get(name=r["asset"])
		BuyOrder.objects.create(
			asset=assetID,
			size=r["size"],
			bid=r["bid"]
		)
	elif r["orderType"] == "sell":
		assetID = Asset.objects.get(name=r["asset"])
		SellOrder.objects.create(
			asset=assetID,
			size=r["size"],
			ask=r["ask"]
		)

	return HttpResponse("hello")

def match(request):
	bids = BuyOrder.objects.filter(status=False).order_by("start")
	asks = SellOrder.objects.filter(status=False).order_by("start")

	for bid in bids:
		print(bid.start)

	print(len(bids), len(asks))

	return HttpResponse("hello")