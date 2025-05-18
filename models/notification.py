from pydantic import BaseModel, EmailStr
from typing import Optional

class NotificationIn(BaseModel):
    user_id: int
    type: str  # email, sms, in-app
    message: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class Notification(NotificationIn):
    pass  # Could extend with id, timestamp, status, etc.
