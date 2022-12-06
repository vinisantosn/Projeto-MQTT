# this file simulates the subscription in the two topics

# libs
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Smartphone-1")
client.connect(mqttBroker) 

client.on_connect = on_connect

client.loop_start()

client.subscribe("SENSOR/#")

client.on_message=on_message 

time.sleep(30)
client.loop_stop()
