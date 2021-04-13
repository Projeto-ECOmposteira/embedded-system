import network

def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
        print('network config:', wlan.ifconfig())

if __name__ == '__main__':

    do_connect('Felipe-ClickNET', 'xrl8clicknet')
