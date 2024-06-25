# MQTT with Python

#### MQTT library for Python and Time library for listening time.
```
import paho.mqtt.client as mqtt 
import time
```
#### MQTT message and listening function from "paho.mqtt.client".
```
def message(random_client_name, c, listen_message):       
    print(str(listen_message.payload.decode("utf-8")))
```
#### Called into "c" MQTT Client method.
```
c = mqtt.Client()  
```
#### Message function called and started wait
```
c.on_message = message  
```
#### Connecting MQTT Broker
```
c.connect("broker.mqttdashboard.com") 
```
#### "GEL" message sent to broker with "ev-ev" topic
```
c.publish("ev-ev","GEL")                
```
#### Client is subscribing "ev-ev-ev" topic for listen to message
```
c.subscribe("ev-ev-ev") 
```
#### Listening Started...
```
c.loop_start()                          
time.sleep(1)    
```
#### Listening Stopped.
```
c.loop_stop()                            
```
