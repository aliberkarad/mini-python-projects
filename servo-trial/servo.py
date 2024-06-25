import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50) 
servo.start(0) 
try:
    while True:
        angle = float(input('Set angle 0 & 180: '))
        servo.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
finally:
    servo.stop()
    GPIO.cleanup()
    print("END")