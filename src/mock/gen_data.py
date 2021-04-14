import json

from time import sleep
from random import random
from umqtt.simple2 import MQTTClient

def create_random_example():

    data = {
        'data1' : random(),
        'data2' : random(),
        'data3' : random(),
        'data4' : random(),
    }

    return json.dumps(data)


def data_gen(samples, sleeptime=1):

    for _ in range(samples):

        sleep(sleeptime)

        yield create_random_example()

if __name__ == '__main__':

    print('error')
    server = '10.0.0.104'
    client_id = 'client1'
    topic = b'notification'
    samples = 10

    client = MQTTClient(client_1, server, port=1883, user='mosquitto')

    client.connect()

    for data in data_gen(samples):
        print('test')

        print(data)

        client.publish(topic, bytes(data))

    client.disconnect()

