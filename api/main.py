from fastapi import FastAPI, HTTPException
from models.notification import Notification, NotificationIn
from queue.producer import send_to_queue

app = FastAPI()

notifications_db = []  # In-memory store

@app.post("/notifications", status_code=201)
async def send_notification(notification: NotificationIn):
    if notification.type not in ('email', 'sms', 'in-app'):
        raise HTTPException(status_code=400, detail="Invalid notification type")
    if notification.type == 'email' and not notification.email:
        raise HTTPException(status_code=400, detail="Email is required for email notifications")
    if notification.type == 'sms' and not notification.phone:
        raise HTTPException(status_code=400, detail="Phone number is required for SMS notifications")

    # Send to RabbitMQ queue
    send_to_queue(notification.dict())

    # Save in memory for retrieval (optional)
    new_notification = Notification(
        user_id=notification.user_id,
        type=notification.type,
        message=notification.message,
        email=notification.email,
        phone=notification.phone
    )
    notifications_db.append(new_notification)

    return {"message": "Notification queued successfully"}

@app.get("/users/{user_id}/notifications")
async def get_user_notifications(user_id: int):
    user_notifications = [n for n in notifications_db if n.user_id == user_id]
    return {"notifications": user_notifications}
