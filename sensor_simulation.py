import json
import random

def simulator(stop_):
    for x in range(0,stop_):
        #print("%s --> %s"%(x,random.triangular(0,150)))
        #print("%s --> %s"%(x,random.randint(0,100)))
        dictt={'carbon_monoxide':{'Useful_detection':random.triangular(0,150),'level':random.randint(0,100)},
        'sulpher_dioxide':{'Useful_detection':random.triangular(0,150),'level':random.randint(0,100)}}
        sensor_json=json.dumps(dictt)
        print(sensor_json)
        print(type(sensor_json))
    return 'done'
simulator(1)