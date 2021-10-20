def publish_sensor(project_id, topic_id,data,origin='python-sample',username='gcp'):
    """"
    description: send data to pubsub topic
    arguments:
        project_id (str): name of GCP project ID
        topic_id (str): name of pubsub topic
        data (str): data you want to upload
        origin (str): name of origin it could be any string
        username (str): name of username it could be any


    returns (str): topic path id
    """
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    data = data.encode("utf-8")
    future = publisher.publish(
        topic_path, data, origin=origin, username=username
    )
    print(future.result())


    return "Published messages with custom attributes to {} ".format(topic_path) 
if __name__ =='__main__':
    publish_sensor("elaborate-howl-285701", "iot-check","hello2")