from machine import TouchPad, Pin
from time import sleep

touch = TouchPad(Pin(4))  

while True:
    print(touch.read())
    sleep(0.5)

#test
