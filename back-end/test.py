import requests
import json
import random 
import time

def newEvent():
	stuff = {
		"num_shares": 5,
		"name": "election"
	} 


	r = requests.post("http://localhost:8000/event/", json=json.dumps(stuff))

def newPlayer(playerName):
	stuff = {
		"name": playerName,
		"overlap": 2,
		"capital": 10,
		"knowledge_size": 4
	} 


	r = requests.post("http://localhost:8000/player/", json=json.dumps(stuff))

def newOrder(playerName, orderType):
	stuff = {
        "player": playerName,
        "event": "election",
        "quantity": 2,
        "price": random.uniform(0.1, 1),
        "status": True,
        "side": True,
        "order_type": orderType
	} 


	r = requests.post("http://localhost:8000/order/", json=json.dumps(stuff))

def match():
	r = requests.get("http://localhost:8000/match/")
	print("price", r.text)

def setup():
	newEvent()
	newPlayer("lorenzo")
	newPlayer("lorenzo2")
	for i in range(5):
		newOrder("lorenzo", True)
	for i in range(5):
		newOrder("lorenzo2", False)
	
setup()
time.sleep(4)
match()
