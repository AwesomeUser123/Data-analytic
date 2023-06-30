import random 
import time 
import sys 
import requests 

from Adafruit_IO import MQTTClient

AIO_FEED_ID="equation"
AIO_USERNAME ="SuSername"
AIO_KEY ="aio_QnTt01i4LBz8TxVW8rMhrWkPK8mc"
global_equation = "x1 + x2 + x3"
def init_global_equation():
    global global_equation
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/SuSername/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)

def message(client , feed_id , payload):
    print("Received: " + payload)
    if(feed_id == "equation"):
        global  global_equation
        global_equation = payload
        print("Nhan du lieu: ",global_equation)
def modify_value(x1, x2, x3):
    result = eval(global_equation)
    print(result)
    return result
def connected(client):
    print("ket noi thanh cong ")
    client.subscribe(AIO_FEED_ID)
def subscribe(client, userdata,mid, granted_qos):
    print("Subscribe thanh cong ")
def disconnected(client):
    print("ngat ket noi")
    sys.exit(1)
def message(client, feed_id, payload):
    print("Nhan du lieu: "+payload)
client=MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect= connected
client.on_disconnect= disconnected 
client.on_message= message
client.on_subscribe= subscribe 
client.connect()
client.loop_background()

while True:
   while True:
    time.sleep(5)
    s1 = random.randint(4,50)
    s2 = random.randint(2,50)
    s3 = random.randint(1,50)
    client.publish("sensor1", s1)
    client.publish("sensor2", s2)
    client.publish("sensor3", s3)
    s4 = modify_value(s1, s2, s3)
    client.publish("sensor4",s4)
    print(s4)
    pass