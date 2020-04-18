import requests
import json

def getFoodItems():
    try:
        response=requests.get("http://localhost:9200/triangle/orderfoods/1")
        res=json.loads(response.text)
        food=res['_source']['fooditems']
        return food
    except:
        return []
