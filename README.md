# Notification_Service_System

## Overview

This project is a **Notification Service System** built using **FastAPI**. It provides API endpoints to:

- Send notifications (Email, SMS, In-app)
- Retrieve notifications for a user

The system is designed with extensibility in mind, including support for queuing (RabbitMQ) and retry logic for failed notifications.

---

## Features

- **Send Notification:** POST `/notifications`
- **Get User Notifications:** GET `/users/{id}/notifications`
- Supports 3 types of notifications: Email, SMS, and In-app
- Bonus (optional): Uses RabbitMQ to queue notifications for processing
- Retry failed notifications with exponential backoff

---

## Folder Structure

```bash
notification_service_system/
├── api/
│ └── main.py # FastAPI app with API routes
├── models/
│ └── notification.py # Pydantic models for request/response validation
├── services/
│ ├── email_service.py # Logic to send Email notifications
│ ├── sms_service.py # Logic to send SMS notifications
│ └── in_app_service.py # Logic to send In-app notifications
├── queue/
│ ├── producer.py # Producer to send messages to the queue
│ └── consumer.py # Consumer to receive and process messages from the queue
├── requirements.txt # Required Python packages
└── README.md # This file
```

---

## Prerequisites

- Python 3.8+
- RabbitMQ (optional but recommended for queuing)
- Git (optional, for cloning repo)

---

## Setup Instructions

### 1. Clone the Repository (Optional)

If you have Git installed, you can clone the repo directly:

```bash
git clone https://github.com/yourusername/notification-system.git
cd notification-system
```
Otherwise, just download and extract the project folder.

---

### 2. Create a Virtual Environment

Creating a virtual environment is important to keep dependencies isolated.

*On Windows (PowerShell):*

```bash
python -m venv venv
.\venv\Scripts\activate
```

*On Mac/Linux:*

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Required Packages

Make sure your virtual environment is activated, then run:

```bash
pip install -r requirements.txt
```

This installs:
- FastAPI (web framework)
- Uvicorn (ASGI server)
- Pydantic (data validation)
- Pika (RabbitMQ client)
- Tenacity (retry logic)

---

### 4. Run the Application

To start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

- The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- The Swagger UI docs can be accessed at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 5. (Optional) Setup RabbitMQ

If you want to use queuing for notifications, install and start RabbitMQ:

*Windows*: Download RabbitMQ from [https://www.rabbitmq.com/install-windows.html](https://www.rabbitmq.com/install-windows.html) and follow the installation steps.

*Linux/Mac*: Use your package manager, e.g.,

```bash
sudo apt-get install rabbitmq-server
sudo service rabbitmq-server start
```

Make sure RabbitMQ server is running before you start the FastAPI app.

---

## Usage Examples

### SEND Notifications

```bash
POST /notifications
Content-Type: application/json

{
  "user_id": 1,
  "type": "email",
  "message": "Your order has shipped!"
}
```

### GET Notifications for a User

```bash
GET /users/1/notifications
```

---

## Notes and Assumptions

- The Email and SMS sending functions are stubbed/mocked. You can replace them with real providers (SendGrid, Twilio, etc.) in the service layer.
- Notification persistence (e.g., DB) is a simple in-memory list for demonstration.
- RabbitMQ queue integration is optional and can be enabled by modifying config and service files.
- Retry logic is implemented using Tenacity for robustness.

---

## Troubleshooting

- If you get errors about missing packages, make sure your virtual environment is activated and you ran `pip install -r requirements.txt`.
- For Windows users having trouble activating the virtual environment, check PowerShell execution policies or try activating in cmd.
- If RabbitMQ connection fails, verify the RabbitMQ service is running and the connection parameters in `queue/producer.py` are correct.

---

## Author

*Name*: `ANKIT BAKSHI`
*Publication Date*: `May 19, 2025`
*E-mail*: [bakshiankit1005@gmail.com](bakshiankit1005@gmail.com)
