from time import sleep
from random import random
from umqtt.simple2 import MQTTClient
from machine import RTC

rtc = RTC()

def create_random_example() -> str:
    """
    Create a JSON string with random
    values
    """

    data = {
        'weight' : random(),
        'ph' : random(),
        'cn' : random(),
        'oxigen' : random(),
        'temperature' : random(),
        'pressure': random(),
        'humidity': random(),
        'co2': random(),
        'timestamp': '%.2d:%.2d:%.2dT%.2d:%.2d:%.2d' % rtc.datetime()[:-2],

    }

    return data

def data_gen(samples: int, sleeptime: int=1) -> str:
    """
    Generate JSON messages with sleeptime has a interval.
    Samples define the number of samples that you want 
    to create.
    """

    for _ in range(samples):

        sleep(sleeptime)

        yield create_random_example()

def data_gen_loop(sleeptime: int=1) -> str:
    """
    Generate JSON messages with sleeptime has a interval.
    """

    while True:

        sleep(sleeptime)

        yield create_random_example()
