# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
from machine import Pin,PWM
from time import sleep
import machine
import time


p15=machine.Pin(15,machine.Pin.OUT)

ledpin=14
ledpin2=2
ledpin4=4
p14=machine.Pin(14, machine.Pin.OUT)
pin = Pin(ledpin, Pin.OUT)
pin4 = Pin(ledpin4, Pin.OUT)

# ESP32
sensor = HCSR04(trigger_pin=12, echo_pin=13, echo_timeout_us=10000)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(0.1)
    
    if distance <=20 and distance > 0:
        servo=machine.PWM(p15)
        buzzer=machine.PWM(p14)
        buzzer.freq(727)
        buzzer.duty(1010)
        pin.value(1)
        pin4.value(0)
        servo.freq(50)
        servo.duty(39)
        time.sleep(1)

        time.sleep(2)
        servo.duty(121)	
        pin.value(0)

        buzzer.deinit()
        
    
