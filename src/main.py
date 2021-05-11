import json
import ubinascii

from util.wifi import auto_connect_wifi
from mock.gen_data import data_gen_loop

from umqtt.simple2 import MQTTClient
from wifi import wifimgr

if __name__ == '__main__':

    wlan = wifimgr.get_connection()

    if wlan is None:
        print("Could not initialize the network connection.")
        while True:
            pass  # you shall not pass :D

    print("Starting Server")

    server = 'test.mosquitto.org'
    client_id = 'composteira1'
    topic = 'ecomposteira/composter/measurements'
    topic = topic.encode()

    client = MQTTClient(client_id, server, port=1883)
    client.connect()

    for data in data_gen_loop(sleeptime=60):

        data['macAddress'] = ubinascii.hexlify(wlan.config('mac'), ':').decode()
        data = json.dumps(data)
        print("Publicando %s" % data)

        client.publish(topic, data)

    client.disconnect()
