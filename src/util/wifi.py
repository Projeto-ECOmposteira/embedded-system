import network
import time

class WifiConnectionError(Exception):
    pass

def connect_wifi(ssid: str, password: str) -> None:
    """
    Try to establish a wifi connection
    The connection loop will end only
    if the connection 
    """

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():

        print('Connecting to network...')

        wlan.connect(ssid, password)

        for _ in range(30):
            if wlan.isconnected()
                sleep(1)
        else:
            raise WifiConnectionError(
                f'Is not possible to stablish a connection \
                with {ssid}, check ssid and password'
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
        
