##  SERVO MOTOR APPLICATION with RASPBERRY PI
### Libraries
```
import RPi.GPIO as GPIO
import time
```
### GPIO pins setup
```
GPIO.setmode(GPIO.BOARD)
```
### GPIO pin 11 set for output
```
GPIO.setup(11,GPIO.OUT)
```
### Pin 11 set for 50Hz PWM signal
```
servo = GPIO.PWM(11,50) 
```
### Servo PWM set to zeroth location
```
servo.start(0)
``` 

```
try:
    while True:
```
###### Asking input and set servo step
```
angle = float(input('Set angle 0 & 180: '))
servo.ChangeDutyCycle(2+(angle/18))
time.sleep(0.5)
servo.ChangeDutyCycle(0)
```

###### Stopped everything
```
finally:
    servo.stop()
    GPIO.cleanup()
    print("END")
```
