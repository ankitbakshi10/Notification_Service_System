from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum

app = FastAPI()
notifications_db = []

# Define notification types as an Enum for validation
class NotificationType(str, Enum):
    email = "email"
    sms = "sms"
    in_app = "in_app"

# Request model for sending notifications
class NotificationIn(BaseModel):
    user_id: int
    type: NotificationType
    message: str
    email: Optional[EmailStr] = None  # Optional, only needed if type=email
    phone_number: Optional[str] = None  # Optional, only needed if type=sms

# Model for storing a notification (simulated in-memory)
class Notification(BaseModel):
    id: int
    user_id: int
    type: NotificationType
    message: str

# Simple in-memory storage for demo purposes
notifications_db: List[Notification] = []
notification_id_counter = 1

# POST /notifications - send notification endpoint
@app.post("/notifications")
def send_notification(notification: NotificationIn):
    global notification_id_counter

    # Validate required info based on type
    if notification.type == NotificationType.email and not notification.email:
        raise HTTPException(status_code=400, detail="Email is required for email notifications")
    if notification.type == NotificationType.sms and not notification.phone_number:
        raise HTTPException(status_code=400, detail="Phone number is required for SMS notifications")

    # Simulate saving notification
    new_notification = Notification(
        id=notification_id_counter,
        user_id=notification.user_id,
        type=notification.type,
        message=notification.message,
    )
    notifications_db.append(new_notification)
    notification_id_counter += 1

    # Here you would add notification to queue or send it directly

    return {"message": "Notification sent", "notification_id": new_notification.id}

# GET /users/{id}/notifications - fetch notifications for a user
@app.get("/users/{user_id}/notifications", response_model=List[Notification])
def get_user_notifications(user_id: int):
    user_notifications = [n for n in notifications_db if n.user_id == user_id]
    return user_notifications
