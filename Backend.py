import requests
import json

ENDPOINT="https://xy1o4m1fg9:gwecxfoo1d@trianglevpa-9475796546.ap-southeast-2.bonsaisearch.net:443"

def getEntityKnowledge():
    try:
        #response=requests.get("http://localhost:9200/triangle/orderfoods/1")
        #Online database added
        response=requests.get(ENDPOINT+"/triangle/orderfoods/1")
        #response=requests.get("https://xy1o4m1fg9:gwecxfoo1d@trianglevpa-9475796546.ap-southeast-2.bonsaisearch.net:443/triangle/orderfoods/1")
        print("Response received ",response.text)
        print(type(response.text))
        res=json.loads(response.text)
        print(type(res))
        food=res['_source']['entityknowledge1']
        return food
    except:
        return []


#https://xy1o4m1fg9:gwecxfoo1d@trianglevpa-9475796546.ap-southeast-2.bonsaisearch.net:443

def recordQuery(msg,code):
    try:
        msg=msg.replace(" ","")
        myobj={"userinput":msg,"eid":code}
        x=requests.post(ENDPOINT+"/triangle_input/userinput",json=myobj)
        print(x.text)
    except:
        print("Eror while logging the logs")



def fetchCode(msg):
    try:
        msg=msg.replace(" ","")
        myobj={"size":0,"query":{"match":{"userinput":msg}},"aggs":{"codenumber":{"terms":{"field":"eid"}}}}
        print("Fetching the code")
        res=requests.get(ENDPOINT+"/triangle_input/userinput/_search",json=myobj)
        print("Response in fetchcode",res.text)
        response=json.loads(res.text)
        CODE=response['aggregations']['codenumber']['buckets']
        if len(CODE)==0:
            #if there is no such msgs before then record the query else use the knowledge
            print("No such msg heard before hence recording this one")
            newinput=requests.post(ENDPOINT+"/triangle_newinput/newinput",json={"userinput":msg})
            return -99
        else:
            #return the knowledge
            print("Knowledge is there")
            return CODE[0]['key']
    except Exception as e:
        return 10
        print(e)



def recordFeedBack(feedback):
    try:
        feedback=feedback.replace(" ","")
        myobj={ "msg":feedback }
        print("Sending Feedback")
        res=requests.post(ENDPOINT+"/triangle_feedback/feedback/",json=myobj)
        print("Response in Feedback",res.text)
    except Exception as e:
        print("Error in feedback sending BAckend")
        print(e)

def loadKnowledge():
    try:
        res=requests.get(ENDPOINT+"/triangle_knowledge/knowledge/1")
        response=json.loads(res.text)
        knowledge=response['_source']['knowledge']
        return knowledge
    except:
        return []












