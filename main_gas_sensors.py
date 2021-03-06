import json
import random
import time
from pubsub import publish_sensor as ps
from datetime import datetime

def simulator():
    project_id = "elaborate-howl-285701"
    topic_id = "iot-check"
    now = str(datetime.now())

    dictt_carbon_mono={'Timestamp':now,'Air_Pollutant':'Carbon_monoxide','Useful_detection':random.triangular(0,0.3),'level':random.randint(0,50)}
    dictt_sulpher_di={'Timestamp':now,'Air_Pollutant':'sulpher_dioxide','Useful_detection':random.triangular(0,100),'level':random.randint(0,100)}
    dictt_carbon_di={'Timestamp':now,'Air_Pollutant':'carbon_dioxide','Useful_detection':random.triangular(350,600),'level':None}
    dictt_nitrogen_di={'Timestamp':now,'Air_Pollutant':'Nitrogen_dioxide','Useful_detection':random.triangular(0,50),'level':random.randint(0,100)}
    dictt_Methane={'Timestamp':now,'Air_Pollutant':'Methane','Useful_detection':random.triangular(1500,2000),'level':None}
    dictt_Volatile={'Timestamp':now,'Air_Pollutant':'Volatile_organic_compounds','Useful_detection':random.triangular(5,100),'level':None}

    sensor_carbon_mono=json.dumps(dictt_carbon_mono)
    print(sensor_carbon_mono)
    ps(project_id,topic_id,sensor_carbon_mono)

    sensor_sulpher_di=json.dumps(dictt_sulpher_di)
    print(sensor_sulpher_di)
    ps(project_id,topic_id,sensor_sulpher_di)

    sensor_carbon_di=json.dumps(dictt_carbon_di)
    print(sensor_carbon_di)
    ps(project_id,topic_id,sensor_carbon_di)

    sensor_nitrogen_di=json.dumps(dictt_nitrogen_di)
    print(sensor_nitrogen_di)
    ps(project_id,topic_id,sensor_nitrogen_di)

    sensor_Methane=json.dumps(dictt_Methane)
    print(sensor_Methane)
    ps(project_id,topic_id,sensor_Methane)

    sensor_Volatile=json.dumps(dictt_Volatile)
    print(sensor_Volatile)
    ps(project_id,topic_id,sensor_Volatile)
        
    return 'status:200'

while True:
    simulator()
    time.sleep(5)



