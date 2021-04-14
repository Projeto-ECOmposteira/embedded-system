import network

def connect_wifi(ssid, password):

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():

        print('Connecting to network...')

        wlan.connect(ssid, password)

        while not wlan.isconnected():
            pass
        
        print('Network settings:', wlan.ifconfig())


def auto_connect_wifi():

    try:
        with open('wifi.cfg', 'r') as configfile:

            lines = configfile.readlines()

            ssid = lines[0].strip()
            password = lines[1].strip()

            connect_wifi(ssid, password)

    except:
        print("Don't have wifi config")
        
