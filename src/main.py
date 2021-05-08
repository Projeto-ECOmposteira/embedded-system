from util.wifi import auto_connect_wifi
from mock.gen_data import data_gen

from umqtt.simple2 import MQTTClient
from wifi import wifimgr

if __name__ == '__main__':

    wlan = wifimgr.get_connection()

    if wlan is None:
        print("Could not initialize the network connection.")
        while True:
            pass  # you shall not pass :D

    print("Starting Server")

    server = '10.0.0.145'
    client_id = 'client1'
    topic = b'notification'

    client = MQTTClient(client_id, server, ssl=False, port=1883)
    client.connect()

    for data in data_gen(30):
        print("Publicando")
        client.publish(topic, data)

    client.disconnect()
