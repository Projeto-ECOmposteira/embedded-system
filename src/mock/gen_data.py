import json

from time import sleep
from random import random
from umqtt.simple2 import MQTTClient

def create_random_example() -> str:
    """
    Create a JSON string with random
    values
    """

    data = {
        'data1' : random(),
        'data2' : random(),
        'data3' : random(),
        'data4' : random(),
    }

    return json.dumps(data)

def data_gen(samples: int, sleeptime: int=1) -> str:
    """
    Generate JSON messages with sleeptime has a interval.
    Samples define the number of samples that you want 
    to create.
    """

    for _ in range(samples):

        sleep(sleeptime)

        yield create_random_example()
