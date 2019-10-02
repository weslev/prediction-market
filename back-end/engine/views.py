from django.shortcuts import render
from .models import Event, Knowledge, Player, Share, Order, OrderLog, Transaction
import json
from django.http import JsonResponse, HttpResponse
import random
from datetime import datetime 
from django.core import serializers


def createEvent(request):
    r = json.loads(request.body)
    r = json.loads(r)
    num_shares = r["num_shares"]
    name = r["name"]
    print(num_shares)

    new_event = Event.objects.create(
        name=name,
        ground_truth = 0
    )

    sides = [True, False]
    for side in sides:
        for i in range(num_shares):
            Share.objects.create(
                asset=side,
                event=new_event
            )

    return HttpResponse("success")

def registerPlayer(request):
    r = json.loads(request.body)
    r = json.loads(r)
    overlap = r["overlap"]
    capital = r["capital"]
    name = r["name"]
    knowledge_size = r["knowledge_size"]

    new_knowledge = knowledge_size - overlap

    #latest_event
    latest_event = Event.objects.last()

    #new player
    new_player = Player.objects.create(
        name=name,
        capital=capital,
    )

    #loop through last player's local knoweldge to get the overlap
    all_current_knowledge = Knowledge.objects.all()
    if len(all_current_knowledge) > overlap:
        for i in range(knowledge_size - overlap):
            index_n = i + 1
            Knowledge.objects.create(
                value = bool(random.randint(0, 1)),
                event = latest_event,
                index = len(all_current_knowledge) + index_n
            )
            i += 1
    else:
        #if not possible, randomly pick values to fill overlap
        for i in range(overlap - len(all_current_knowledge)):
            index_n = i + 1
            Knowledge.objects.create(
                value = bool(random.randint(0, 1)),
                event = latest_event,
                index = len(all_current_knowledge) + index_n
            )
        #for item in new_knowledge, randomly pick a value to generate new knowledge 
        all_current_knowledge = Knowledge.objects.all()
        for i in range(knowledge_size - overlap):
            index_n = i + 1
            Knowledge.objects.create(
                value = bool(random.randint(0, 1)),
                event = latest_event,
                index = len(all_current_knowledge) + index_n
            )

    all_current_knowledge = Knowledge.objects.all()
    local_knowledge = Knowledge.objects.all()[(len(all_current_knowledge) - knowledge_size): (len(all_current_knowledge) - 1)]


    new_player.local_info.add(*local_knowledge)

    new_player.events.add(latest_event)

    return HttpResponse("success")

def order(request):
    r = json.loads(request.body)
    r = json.loads(r)
    player = r["player"]
    order_type = r["order_type"] #buy or sell
    asset  = r["side"]
    quantity = r["quantity"]
    price = r["price"]
    event = r["event"]
    side = r["side"]

	#log order
    OrderLog.objects.create(
        player = Player.objects.get(name=player),
        event = Event.objects.get(name=event),
        quantity = quantity,
        price = price,
        side = side,
        order_type = order_type
    )

    for i in range(quantity):
        Order.objects.create(
            player = Player.objects.get(name=player),
            event = Event.objects.get(name=event),
            price = price,
            status = True,
            side = side,
            order_type = order_type
        )

    return HttpResponse("success")

def findBreakEvenIndex(buyers, sellers):
    breakEvenIndex = 0
    for i in range(max(len(buyers), len(sellers))):
        breakEvenIndex = i
        if buyers[i].price < sellers[i].price:
            break
    return breakEvenIndex


def orderMarket():
    #buyers = buyers[:]
    buyers = Order.objects.filter(order_type=True).filter(status=True).order_by("price")
    buyers = list(reversed(buyers))
    #sellers = sellers[:]
    sellers = Order.objects.filter(order_type=False).filter(status=True).order_by("price")
    #sort for time in case of equal prices 
    #https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
    return buyers, sellers


def match(request):
    print("triggered")
    (orderedBuyers, orderedSellers) = orderMarket()
    for order in orderedBuyers:
        print(order.player, order.price)
    print("---")
    for order in orderedSellers:
        print(order.player, order.price)
    breakEvenIndex = findBreakEvenIndex(orderedBuyers, orderedSellers)
    print("breakEvenIndex", breakEvenIndex)
    price = (orderedBuyers[breakEvenIndex].price + orderedSellers[breakEvenIndex].price) / 2.0

    #this is just for testing
    for share in Share.objects.all():
        share.owner = orderedSellers[0].player
        share.save()

    for i in range(breakEvenIndex + 1):

        share = Share.objects.filter(owner=orderedSellers[i].player)[0]

        print(i, breakEvenIndex, price)

        #make a transaction(buyer.pop(0), seller.pop(0), seller.share, price)
        Transaction.objects.create(
            share=share,
            buyer=orderedBuyers[i].player,
            seller=orderedSellers[i].player,
            price=price
        )

        seller = orderedSellers[i].player
        seller.capital += price
        seller.save()

        buyer = orderedBuyers[i].player
        buyer.capital -= price
        buyer.save()


        #order where player = seller, order.quantity - 1, if order.quantity = 0, status = False and closingTime = timestamp
        #order where player = buyer, order.quantity - 1, if order.quantity = 0, status = False and closingTime = timestamp
        orderedSellers[i].status = False
        orderedSellers[i].closingTime = datetime.now()

        orderedBuyers[i].status = False
        orderedBuyers[i].closingTime = datetime.now()

        #share where owner = seller, share.owner = buyer and share.price = price
        share.owner = orderedBuyers[i].player
        share.price = price
        share.save()

    return HttpResponse(price)

def engine(batch_size):
	#if orders where order.status == active >= batch_size, match(orders where order.type = buy, orders where order.type = sell)
    print("hello")

def oracle(request):
    r = json.loads(request.body)
    data_spec = r["spec"]
    data_to_return = {}
    if data_spec == "transactions":
        txs = Transaction.objects.all()
        i = 0
        for tx in txs:
            ob = {}
            ob["event"] = tx.share.event.name
            ob["side"] = tx.share.asset
            ob["price"] = tx.price
            data_to_return[i] = ob
            i += 1
    print(data_to_return)
    return JsonResponse(data_to_return)
