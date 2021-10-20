from google.cloud import pubsub_v1


project_id = "elaborate-howl-285701"
topic_id = "iot-check"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 10):
    data = f"Message number {n}"
    # Data must be a bytestring
    data = data.encode("utf-8")
    # Add two attributes, origin and username, to the message
    future = publisher.publish(
        topic_path, data, origin="python-sample", username="gcp"
    )
    print(future.result())

print(f"Published messages with custom attributes to {topic_path}.")