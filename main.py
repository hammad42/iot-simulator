from google.cloud import pubsub_v1
import json
import random
import time

def simulator(stop_):
    project_id = "elaborate-howl-285701"
    topic_id = "iot-check"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    for x in range(0,stop_):

        dictt_carbon_mono={'Air_Pollutant':'Carbon_monoxide','Useful_detection':random.triangular(0,0.3),'level':random.randint(0,50)}
        dictt_sulpher_di={'Air_Pollutant':'sulpher_dioxide','Useful_detection':random.triangular(0,100),'level':random.randint(0,100)}
        dictt_carbon_di={'Air_Pollutant':'carbon_dioxide','Useful_detection':random.triangular(350,600),'level':'None'}
        dictt_nitrogen_di={'Air_Pollutant':'Nitrogen_dioxide','Useful_detection':random.triangular(0,50),'level':random.randint(0,100)}
        dictt_Methane={'Air_Pollutant':'Methane','Useful_detection':random.triangular(1500,2000),'level':'None'}
        dictt_Volatile={'Air_Pollutant':'Volatile_organic_compounds','Useful_detection':random.triangular(5,100),'level':'None'}

        sensor_json=json.dumps(dictt)
        print(sensor_json)
        print(type(sensor_json))
    return sensor_json




while True:
    data = simulator(1)
    # Data must be a bytestring
    data = data.encode("utf-8")
    # Add two attributes, origin and username, to the message
    future = publisher.publish(
        topic_path, data, origin="python-sample", username="gcp"
    )
    print(future.result())

    print(f"Published messages with custom attributes to {topic_path}.")
    time.sleep(5) # Sleep for 5 seconds