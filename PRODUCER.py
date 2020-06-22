#import libraries
import time
from time import sleep
from kafka import KafkaProducer
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import sys
import random
import json

'''Reading keys and getting data from alphavintage'''
def take_data():
    try:
        ticker = 'GOOGL'
        lines = open('keys').read().splitlines()
        keys = random.choice(lines)
        time = TimeSeries(key=keys,output_format='json')
        data , metadata = time.get_intraday(symbol= ticker,interval='1min',outputsize='full')
        return data
    except:
        print("keys not found")

'''sending data to kafka messaging unit '''

def publish_message(producerkey, key, data_key):
    from json import dumps
    key_bytes = bytes(key, encoding='utf-8')
    producerkey.send("stock", json.dumps(data[key]).encode('utf-8'), key_bytes)
    print("message published")

'''Establish connection for producer'''
def kafka_producer_connection():
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        return producer
    except:
        print("connection unsuccessful")

if __name__ == "__main__":
    data = take_data()
    if len(data) > 0:
        kafka_producer = kafka_producer_connection()
        for key in sorted(data):
            publish_message(kafka_producer, key, data[key])
            sleep(2)
