import json
import random
import time
from pubsub import publish_sensor as ps
from datetime import datetime 


def simulator():
    project_id = "elaborate-howl-285701"
    topic_id = "iot-check_renewable"
    now = str(datetime.now())
    dictt_renewable={'Timestamp':now,'Siemens_WindTurbine_KW':random.triangular(10,18),'GE_WindTurbine_KW':random.triangular(9,15),
    'Prism_Solar_1_KW':random.triangular(0.7,4),'Prism_Solar_2_KW':random.triangular(0.5,3)}


    sensor_renewable=json.dumps(dictt_renewable)
    print(sensor_renewable)
    ps(project_id,topic_id,sensor_renewable)

        
    return 'status:200'

while True:
    simulator()
    time.sleep(5)



