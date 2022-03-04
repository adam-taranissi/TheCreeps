import pandas as pd
import paho.mqtt.client as mqtt
import time



data = pd.read_excel("shodan_query_results.xlsx")
print(data.head(5))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # Subscribe to EVERYTHING 
    #client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("\ntopic: ", msg.topic)
    print("\npayload: ",str(msg.payload.decode("ASCII")))
    print("\nmessage qos: ",msg.qos)
    print("\nmessage retain flag: ",msg.retain)
    print("*****************************")

def on_publish(client,userdata,result):
    print("data published \n")
    

client = mqtt.Client()
print("Created new client instance\n")
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

#hardcoding a specific IP bc it looked juicy
print(data['IP'][90])
print("connecting to broker\n")
client.connect(data['IP'][90], 1883, 60)
client.loop_start()
print("subscribing to topic\n")
client.subscribe("7c:df:a1:40:fc:70/schedule/20")
print("publishing a message...\n")
result = client.publish("7c:df:a1:40:fc:70/schedule/20","you might want to disable anonymous connections to your MQTT device")[0]
print("Result code is: ", result)
time.sleep(3)
client.loop_stop()

def on_disconnect(client, userdata, rc):
   print("client disconnected ok")
client.on_disconnect = on_disconnect
client.disconnect()

