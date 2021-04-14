import network
from time import sleep

class WifiConnectionError(Exception):
    pass

def connect_wifi(ssid: str, password: str) -> None:
    """
    Try to establish a wifi connection
    The connection loop for 30 second
    until establish a connection
    """

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)


    print('Connecting to network...')

    if not wlan.isconnected():

        wlan.connect(ssid, password)

        for _ in range(30):
            if not wlan.isconnected():
                sleep(1)
            else:
                break

    else:
        raise WifiConnectionError(
            "Is not possible to stablish a connection \
            with %s, check ssid and password" % ssid
        )

    print('Network settings:', wlan.ifconfig())

def auto_connect_wifi() -> None:
    """
    Extract ssid and password information 
    from wifi.cfg file. After that uses
    connect_wifi function
    """

    try:
        with open('wifi.cfg', 'r') as configfile:

            lines = configfile.readlines()

            ssid = lines[0].strip()
            password = lines[1].strip()

            connect_wifi(ssid, password)

    except Exception as error:

        print("Don't have wifi config")

        raise error
        
