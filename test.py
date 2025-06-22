import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
nets = wlan.scan()

for net in nets:
    print("SSID:", net[0].decode(), "Signal:", net[3])
