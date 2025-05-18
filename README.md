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
notification-system/
├── api/
│ └── main.py # FastAPI app with API routes
├── core/
│ ├── config.py # Configuration variables (like RabbitMQ, DB settings)
│ └── queue.py # RabbitMQ connection and queue helpers
├── services/
│ ├── notification_service.py # Logic to send and retry notifications
│ └── retry.py # Retry logic using Tenacity
├── models/
│ └── notification.py # Pydantic models for request/response validation
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

