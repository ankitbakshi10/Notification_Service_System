import pika
import json

def send_to_queue(notification: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notification_queue', durable=True)

    message = json.dumps(notification)
    channel.basic_publish(
        exchange='',
        routing_key='notification_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    connection.close()
