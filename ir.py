
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
irpin = 26
servoPIN = 21


GPIO.setup(irpin, GPIO.IN)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
angle = 5
st = True
plus = True
p.start(0)
try:
    while True:
        x = GPIO.input(irpin)
        #print(x)
        time.sleep(0.5)
        if x == 1:
           print("X")
           p.ChangeDutyCycle(1)

        else:
           print("O")
           if angle >=12:
               plus = False
           if angle <= 1:
               plus = True
           if plus:
               angle +=1
           else:
               angle -=1
           p.ChangeDutyCycle(11)
           time.sleep(1)
           #p.ChangeDutyCycle(7.5)
           #time.sleep(1)
           #p.ChangeDutyCycle(12)
           #time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
