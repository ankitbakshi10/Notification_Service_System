import pika
import json
from services.email_service import send_email
from services.sms_service import send_sms
from services.in_app_service import send_in_app
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def process_notification(notification):
    notif_type = notification['type']
    if notif_type == 'email':
        if not notification.get('email'):
            raise ValueError("Missing email")
        success = send_email(notification['email'], notification['message'])
    elif notif_type == 'sms':
        if not notification.get('phone'):
            raise ValueError("Missing phone")
        success = send_sms(notification['phone'], notification['message'])
    elif notif_type == 'in-app':
        success = send_in_app(notification['user_id'], notification['message'])
    else:
        raise ValueError("Invalid notification type")

    if not success:
        raise Exception("Sending failed")
    print(f"Notification processed successfully: {notification}")

def callback(ch, method, properties, body):
    notification = json.loads(body)
    try:
        process_notification(notification)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Failed to process notification: {e}")
        # Message will be requeued by RabbitMQ if not acked

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notification_queue', durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='notification_queue', on_message_callback=callback)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
