import paho.mqtt.client as mqtt
import time
###########################################
def message(random_client_name, c, listen_message):
    print(str(listen_message.payload.decode("utf-8")))
###########################################
c = mqtt.Client()
###########################################
c.on_message=message
###########################################
c.connect("broker.mqttdashboard.com")
###########################################
c.publish("ev-ev","GEL")
###########################################
c.subscribe("ev-ev-ev")
c.loop_start() 
time.sleep(1)
c.loop_stop()
###########################################
