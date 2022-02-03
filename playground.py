import pandas as pd
import paho.mqtt.client as mqtt



data = pd.read_excel("Data\shodan_query_results.xlsx")
print(data.head(5))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # Subscribe to EVERYTHING 
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("ASCII")))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#hardcoding a specific IP bc it looked juicy
print(data['IP'][90])
client.connect(data['IP'][90], 1883, 60)
client.loop_forever()
