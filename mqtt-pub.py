# libs

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

# broker - MQTT

mqttBroker ="mqtt.eclipseprojects.io" 

client = mqtt.Client("Temperature")
client.connect(mqttBroker) 

while True:
    randNumberTemp = uniform(26.0, 28.0)
    client.publish("SENSOR/TEMPERATURE", round(randNumberTemp,4))
    print("Just published " + str(round(randNumberTemp,4)) + " to topic TEMPERATURE")

    randNumberHumd = uniform(75, 80)
    client.publish("SENSOR/HUMIDITY", round(randNumberHumd,2))
    print("Just published " + str(round(randNumberHumd,2)) + " to topic HUMIDITY")
    time.sleep(1)



