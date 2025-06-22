MicroPython Examples for ESP32
This repository features basic MicroPython examples for the ESP32, covering TouchPad usage, LED control, and Wi-Fi scanning.

Getting Started
Before you begin, make sure you have MicroPython installed on your ESP32. If not, check out the MicroPython documentation for installation instructions.

Examples
1. Touch Pad Reader
This script reads and displays the touch sensor values from GPIO 4 every half-second.

Hardware:

ESP32 board

A touch-sensitive pad or wire connected to GPIO 4

Code:

from machine import TouchPad, Pin
from time import sleep

touch = TouchPad(Pin(4))

while True:
    print(touch.read())
    sleep(0.5)


Usage:
Upload this script to your ESP32. You'll see the sensor values change in your serial monitor when the touch pad is activated.

2. LED Blinker
This script makes an LED connected to GPIO 2 blink on and off every second.

Hardware:

ESP32 board

An LED

A current-limiting resistor (e.g., 220 Ohm)

Jumper wires

Wiring:
Connect the anode (longer leg) of your LED to GPIO 2 (via the resistor) and the cathode (shorter leg) to GND.

Code:

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(1) # Turn LED on
    sleep(1)
    led.value(0) # Turn LED off
    sleep(1)


Usage:
Upload this script to your ESP32, and the LED connected to GPIO 2 will begin blinking.

3. Wi-Fi Scanner
This script scans for nearby Wi-Fi networks and then prints their SSIDs and signal strengths.

Hardware:

ESP32 board (Wi-Fi capabilities are built-in)

Code:

import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
nets = wlan.scan()

for net in nets:
    print("SSID:", net[0].decode(), "Signal:", net[3])


Usage:
Upload this script to your ESP32. When it runs, it will display a list of available Wi-Fi networks and their signal strengths in your serial monitor.

Contributing
Feel free to expand on these examples or add new ones! Pull requests are always welcome.
