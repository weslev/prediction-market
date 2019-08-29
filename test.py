import requests
import json 

stuff = {
	"asset": "dodgecoin",
	"orderType": "sell",
	"size": 5,
	"ask": 0.3
} 


# r = requests.post("http://localhost:8000/order/", json=json.dumps(stuff))

r = requests.get("http://localhost:8000/match/")