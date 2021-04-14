from util.wifi import auto_connect_wifi
from mock.gen_data import data_gen

from umqtt.simple2 import MQTTClient

if __name__ == '__main__':

    # try to create wifi connection
    auto_connect_wifi()

    server = '10.0.0.105'
    client_id = 'client1'
    topic = b'notification'

    client = MQTTClient(client_id, server, ssl=False, port=1883)
    client.connect()

    for data in data_gen(30):
        client.publish(topic, data)

    client.disconnect()
